from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("261016_4_yolo_advan/heatmap_video.mp4")

# 2. 모델 로드 (show=True 대신 False로 두고 우리가 직접 안전하게 화면에 띄웁니다)
heatmap = solutions.Heatmap(
    model="yolo11n.pt",
    show=False,
    colormap=cv2.COLORMAP_MAGMA
)

# 창 미리 생성
cv2.namedWindow("HEATMAP", cv2.WINDOW_NORMAL)

# 3. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 확인 해주세요")
        break

    # 3-1. 모델 추론 (히트맵이 그려진 프레임을 받아옵니다)   
    results = heatmap(frame)

    # 3-2. 처리된 프레임 표시 (결과가 존재할 때만 안전하게 출력)
    if results is not None:
        cv2.imshow("HEATMAP", results)

    # 3-3. q키를 눌러 종료 (지연 시간을 30ms로 주어 q키 인식이 잘 되도록 수정)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        print("q키를 눌러서 종료")
        break

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()