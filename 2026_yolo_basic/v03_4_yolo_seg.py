from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolov8n-seg.pt")
# 탐지(det) - 물체 주변에 네모 박스만 그림
# 분할(seg) - 물체 모양 그대로 색칠(픽셀 단위)

# 2. 모델 추론
model("2026_python/2026_yoio_basic/peoples.mp4", save = True, show = True)
