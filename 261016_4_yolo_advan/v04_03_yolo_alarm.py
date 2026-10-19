from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
stream_url = "261016_4_yolo_advan/14737135_3840_2160_60fps.mp4"
cap = cv2.VideoCapture(stream_url)  # [수정] 괄호 안에 stream_url 추가

# 2. 이메일 정보 설정
from_email = "skdpfls1106@gmail.com"
password = "vcvk yaag itgm boam"
to_email = "skdpfls1106@gmail.com"

# 3. 모델 로드(알람 객체 생성)
google_alarm = solutions.SecurityAlarm(
    model="yolo11n.pt",   
    show=False,
    classes=[2],          
    records=3             # 3개 이상 탐지되면 메일 1회 전송
)

# 4. SMTP 서버 인증
google_alarm.authenticate(from_email, password, to_email)

# 5. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 확인")
        break

    # 5-1. 모델 추론
    results = google_alarm(frame)

    # 5-2. 윈도우 창 표시
    cv2.imshow("SECURITY_ALARM", results.plot_im)

    # 5-3. q키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q 키를 눌러서 종료")
        break

# 6. 자원 해제
cap.release()
cv2.destroyAllWindows()

# 메일 알람 올 떄 문구를 수정합니다 => 전체 경고임으로 주의해주세요