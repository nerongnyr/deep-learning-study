import cv2
import os
from datetime import datetime
import schedule

# 사진 캡처 간격 설정
interval_time = 5

def take_photo(save_dir="./captured_images"):
    os.makedirs(save_dir, exist_ok=True)
    cap = cv2.VideoCapture(0)
    
    success, frame = cap.read()
    if success:
        path = os.path.join(save_dir, f"{datetime.now().strftime('%Y%m%d_%H%M')}.jpg")
        cv2.imwrite(path, frame)
        print(f"저장 완료: {path}")
    else:
        print("촬영 실패")
        
    cap.release()

# 스케줄러 설정과 무한 루프는 함수 바깥에 위치
schedule.every(interval_time).seconds.do(take_photo)

while True:
    schedule.run_pending()