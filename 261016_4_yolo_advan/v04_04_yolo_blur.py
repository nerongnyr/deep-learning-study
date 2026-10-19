from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("261016_4_yolo_advan/14737135_3840_2160_60fps.mp4")

#모델 로드
blurrer = solutions.ObjectBlurrer(

    model="yolo11n.pt",
    show=False,
    conf=0.6,
    bulf_raflo
)

# 3. 프레임 처리
