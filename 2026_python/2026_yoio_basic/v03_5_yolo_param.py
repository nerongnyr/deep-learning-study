from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolov8n.pt")

# 2. 모델 추론 (파라미터 튜닝)
model(
    "2026_python/2026_yoio_basic/input_param.jpg",
    save = True,
    conf = 0.3,  # 신뢰도 30% 이상
    # max_det = 2 # 최대 탐지 개수 설정
    save_crop = True, # 탐지 영역 이미지 저장
    save_txt = True, # 좌표 텍스트 저장
)