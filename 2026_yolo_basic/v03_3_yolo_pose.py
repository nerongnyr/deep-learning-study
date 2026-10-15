from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolov8n-pose.pt")

# 2. 모델 추론
model("2026_python/2026_yoio_basic/yogav.mp4", save = True)
