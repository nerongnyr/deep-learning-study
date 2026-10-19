from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("261016_4_yolo_advan/14737135_3840_2160_60fps.mp4")

# 2. 영역 좌표 설정 (리스트 형태)
region_points = {
    "region1" :[(538, 283), (538, 94), (98, 79), (71, 362)],
    "region2" :[(538, 283), (538, 94), (98, 79), (71, 362), (138, 28), (89, 54), (456,321), (571, 416)]
}
# 클릭된 좌표는 (538, 283)입니다.
# 클릭된 좌표는 (538, 94)입니다.
# 클릭된 좌표는 (98, 79)입니다.
# 클릭된 좌표는 (71, 362)입니다.

# 3. 모델 로드
yolo_region = solutions.RegionCounter(
    model="yolo11n.pt",
    show=True,
    region=region_points
)

# 4. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임이 더 이상 없거나 불러오지 못했습니다.")
        break

    # 4-1. 프레임 크기 조정 (좌표계 통일)
    re_frame = cv2.resize(frame, (640, 480))

    # 4-2. 구역 내 객체 수 계산 및 자동 시각화 출력
    yolo_region(re_frame)

    # 4-3. q 키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q 키를 눌러서 종료합니다.")
        break
    
# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()