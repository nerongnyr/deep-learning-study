from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolov11n.pt")

# 2. 모델 추론 (파라미터 튜닝)
model(
    "2026_python/2026_yoio_basic/input_want.jpg",
    classes = [55],
    save = True,
    # show = True,
    # conf = 0.1,  # 신뢰도 10% 이상
    # max_det = 2 # 최대 탐지 개수 설정
    # save_crop = True, # 탐지 영역 이미지 저장
    # save_txt = True, # 좌표 텍스트 저장
)