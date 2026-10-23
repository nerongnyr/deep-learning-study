"""CCTV 영상 분석 서버: 영상을 올리면 YOLO로 사람/차량을 찾아 JSON으로 돌려준다."""
import os
import threading
import uuid

import cv2
from flask import Flask, jsonify, request, send_file, send_from_directory
from ultralytics import YOLO

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
UPLOADS = os.path.join(HERE, "uploads")
MODEL_PATH = os.path.join(ROOT, "yolo11n.pt")
SAMPLE_PATH = os.path.join(ROOT, "261016_4_yolo_advan", "14737135_3840_2160_60fps.mp4")

# COCO 클래스 번호 -> 화면에서 쓰는 묶음 (0 사람, 1 차량, 2 이륜차)
GROUP_OF = {0: 0, 2: 1, 5: 1, 7: 1, 1: 2, 3: 2}
SAMPLES_PER_SEC = 5

os.makedirs(UPLOADS, exist_ok=True)
app = Flask(__name__, static_folder="static", static_url_path="/static")
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 1024

model = YOLO(MODEL_PATH)
model_lock = threading.Lock()
jobs = {}  # job_id -> {"state", "progress", "video", "result", "error"}


def analyze(job_id, path):
    job = jobs[job_id]
    try:
        cap = cv2.VideoCapture(path)
        fps = cap.get(cv2.CAP_PROP_FPS) or 30
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 1
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        cap.release()
        if not width or not height:
            raise ValueError("영상을 읽을 수 없습니다")

        stride = max(1, round(fps / SAMPLES_PER_SEC))
        frames = []
        with model_lock:
            stream = model.track(
                path, stream=True, persist=True, vid_stride=stride,
                classes=list(GROUP_OF), conf=0.3, imgsz=640, verbose=False,
            )
            for i, r in enumerate(stream):
                dets = []
                if r.boxes is not None and len(r.boxes):
                    ids = r.boxes.id.int().tolist() if r.boxes.id is not None else [-1] * len(r.boxes)
                    for (x1, y1, x2, y2), c, tid in zip(r.boxes.xyxyn.tolist(), r.boxes.cls.int().tolist(), ids):
                        dets.append([GROUP_OF[c], tid, round(x1, 4), round(y1, 4), round(x2, 4), round(y2, 4)])
                frames.append({"t": round(i * stride / fps, 3), "d": dets})
                job["progress"] = min(0.99, (i + 1) * stride / total)

        job["result"] = {
            "duration": round(total / fps, 2),
            "width": int(width),
            "height": int(height),
            "frames": frames,
        }
        job["progress"] = 1
        job["state"] = "done"
    except Exception as e:  # 사용자에게 원인을 그대로 보여준다
        job["state"] = "error"
        job["error"] = str(e)


def start_job(path):
    job_id = uuid.uuid4().hex[:12]
    jobs[job_id] = {"state": "running", "progress": 0, "video": path, "result": None, "error": None}
    threading.Thread(target=analyze, args=(job_id, path), daemon=True).start()
    return job_id


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.post("/api/analyze")
def api_analyze():
    f = request.files.get("video")
    if not f or not f.filename:
        return jsonify(error="영상 파일을 선택해 주세요"), 400
    ext = os.path.splitext(f.filename)[1].lower()
    if ext not in (".mp4", ".webm", ".mov", ".m4v"):
        return jsonify(error="mp4, webm, mov 파일만 올릴 수 있습니다"), 400
    path = os.path.join(UPLOADS, uuid.uuid4().hex[:12] + ext)
    f.save(path)
    return jsonify(job=start_job(path))


@app.post("/api/sample")
def api_sample():
    if not os.path.exists(SAMPLE_PATH):
        return jsonify(error="샘플 영상을 찾을 수 없습니다"), 404
    return jsonify(job=start_job(SAMPLE_PATH))


@app.get("/api/jobs/<job_id>")
def api_job(job_id):
    job = jobs.get(job_id)
    if not job:
        return jsonify(error="분석 작업을 찾을 수 없습니다. 영상을 다시 올려 주세요"), 404
    out = {"state": job["state"], "progress": job["progress"], "error": job["error"]}
    if job["state"] == "done":
        out["result"] = job["result"]
    return jsonify(out)


@app.get("/api/jobs/<job_id>/video")
def api_video(job_id):
    job = jobs.get(job_id)
    if not job:
        return jsonify(error="분석 작업을 찾을 수 없습니다"), 404
    return send_file(job["video"], conditional=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005, debug=False, threaded=True)
