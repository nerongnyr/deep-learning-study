from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolov8s.pt")

# 2. 모델 추론
results = model("2026_python/2026_yoio_basic/catdog.mp4")

# 3. 결과 시각화
result_image = results[0].plot()

# 4. 결과 이미지 저장
output_result_image_path = "./output_detvs.jpg"
cv2.imwrite(output_result_image_path, result_image)

print(f"결과 이미지가 잘 저장되었습니다: {output_result_image_path}")