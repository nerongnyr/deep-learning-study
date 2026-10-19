from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("261016_4_yolo_advan/14737135_3840_2160_60fps.mp4")

# 2. 라인 설정
line_prints = [(129, 197), (498, 268)]
# 클릭된 좌표는 (129, 197)입니다.
# 클릭된 좌표는 (498, 268)입니다.

# 3. 모델 로드
yolo_counter = solutions.ObjectCounter(
    model="yolo11n.pt",
    region=line_prints
)

# 4. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임이 확인해주세요.")
        break

    # 4-1. 프레임 리사이즈
    re_frame = cv2.resize(frame, (640, 480))

    # 4-2. 구역 내 객체 수 계산 및 자동 시각화 출력
    results =yolo_counter(re_frame)

    # 4-3. 윈도우 창 띄우기
    cv2.imshow("IN/OUT", results.plot_im)

    # 4-3. q 키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q 키를 눌러서 종료합니다.")
        break
    
# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()