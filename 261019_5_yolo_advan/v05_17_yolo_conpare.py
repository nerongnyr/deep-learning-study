from ultralytics import YOLO
import time
import cv2

# 1 비디오 경로 설정
cap = cv2.VideoCapture("261016_4_yolo_advan/heatmap_video.mp4")

# 2 모델 설명
model = YOLO("yolo11n.pt")

# 3 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 확인해주세요")
        break

    # 3-1. 추론 시간 측정
    start_time = time.perf_counter()

    # 3-2 모델 추론
    results = model(frame, verbose=False)

    # 3-3 추론 종료 시간 측정
    end_time = time.perf_counter()

    # 3-4 FPS 계산
    infer_time = end_time - start_time
    fps = 1 / infer_time if infer_time > 0 else 0

    # 3-5 결과 시각화
    annotated_frame = results[0].plot()

    # 3-6 FPS 표시 (오타 및 괄호 구조 수정)
    cv2.putText(
        annotated_frame,
        f"FPS: {fps:.2f}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # 3-7 윈도우 띄우기
    cv2.imshow("YOLO_FPS", annotated_frame)

    # q 키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q 키를 눌러서 종료합니다.")
        break

# 4 자원 해제
cap.release()
cv2.destroyAllWindows()