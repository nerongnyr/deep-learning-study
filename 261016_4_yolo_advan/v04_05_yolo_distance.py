from ultralytics import solutions
import cv2


# 1. 비디오 경로 설정
stream_url = "http://210.99.70.120:1935/live/cctv009.stream/playlist.m3u8"
cap = cv2.VideoCapture(stream_url)

# 2. 모델 로드
distance = solutions.DistanceCalculation(
    model="yolo11n.pt",
    show=True,
    conf=0.05
)

# 3, 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 읽기 실패")
        break

    # 3-1. 모델 추론
    _ = distance(frame)

    pixel_dist = 40  # 예시 값 (단위: px)

    if pixel_dist > 0:
        if pixel_dist < 50:
            # 픽셀 거리가 매우 가까울 때 (위험 단계)
            print(f"[위험] 거리가 너무 가깝습니다! ({pixel_dist:.1f} px)")
        elif 50 <= pixel_dist < 150:
            # 픽셀 거리가 보통일 때 (주의 단계)
            print(f"[주의] 접근 중입니다. 확인이 필요합니다. ({pixel_dist:.1f} px)")
        else:
            # 픽셀 거리가 멀 때 (안전 단계)
            print(f"[안전] 충분한 거리가 유지되고 있습니다. ({pixel_dist:.1f} px)")

    # 3-2. q 키로 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q 키를 눌러서 종료")
        break


# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()

## 픽셀 거리 단위에 따른 상태 정의
