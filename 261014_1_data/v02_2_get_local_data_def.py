import cv2
import os
from datetime import datetime

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

take_photo()