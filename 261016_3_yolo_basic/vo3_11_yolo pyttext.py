from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. URL 설정
stream_url = ""
cv2.VideoCapture(stream_url)

#  3. 실시간 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 또는 주소 확인")
        break
    # 성공했을 때
    # 3-1. 모델 추론
    results = model(frame, conf=0.2)

    # 3-2 박스가 그려진 프레임 얻기
    annotated_frame = results[0].plot()

    # 3-3. 표시할 값 설정
    count = len(results[0])

    # 탐지 개수에 따라 상태 색상 변경
    if count == 0:
        status = "Safe(안전)"
        color = (0, 255, 0)     # 초록색(BGR)
    elif 1 <= count <= 2:
        status = "Warning(주의)"
        color = (0, 255, 255)   # 노란색(BGR)
    else:
        status = "Danger(위험)"
        color = (0, 0, 255)     # 빨간색(BGR)

    #  3-4. 탐지 객체 수 및 상태 화면에 표시
    cv2.putText(
        annotated_frame,   # 텍스트 표시할 영상
        f"{count}, {status}",   # 표시할 텍스트
        (10, 30),   # 표시할 텍스트 위치 좌표
        cv2.FONT_HERSHEY_SIMPLEX,   # 택스트 폰트 스타일
        1,   # 폰트 크기
        color,   # 글자색
        2,# 글자 두께
        cv2.LINE_AA   # 안티엘리어싱
    )

    # 3-5. 윈도우 창 출력
    cv2.imshow("CCTV_YOLO", annotated_frame)

    # 3-6. q키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료합니다.")
        break

#  지원 해제
cap.release()
cv2.destroyAllWindows()

# 탐지 개수에 따른 색상과 상태 병경 조건문 코드 추가