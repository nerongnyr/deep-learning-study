from ultralytics import YOLO
import cv2

# YOLO 모델 로드
# YOLO("모델명")
model = YOLO("yolov8n.pt")
# n -> s -> m -> l -> x

# 모델 추론
results = model("C:\\Users\\Woori\\Desktop\\woori\\2026_python\\2026_yoio_basic\\puppy.jpg")

# 결과 시각화
result_image = results[0].plot()

# 결과 이미지 저장
output_result_image_path = "./output.jpg"
cv2.imwrite(output_result_image_path, result_image)

print(f"예측 결과 이미지가 잘 저장되었습니다 {output_result_image_path}")