import cv2
import matplotlib.pyplot as plt
from PIL import ImageOps

# 1. 이미지 로드
img = cv2.imread("./2026_python/2026_data/captured_images/other_3.jpg")

# 2. 이미지 증강
# 밝기
img_bright = cv2.convertScaleAbs(img, alpha=1, beta=50)
# 대비
img_contrast = cv2.convertScaleAbs(img, alpha=1, beta=50)

# 3. 이미지 시각화
fig, ax = plt.subplots(2, 2, figsize=(10, 5))

# 3-1. 원본 이미지 (왼쪽 위)
ax[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0, 0].axis('off')
ax[0, 0].set_title("original")

# 3-2. 밝기 이미지 (오른쪽 위)
ax[0, 1].imshow(cv2.cvtColor(img_bright, cv2.COLOR_BGR2RGB))
ax[0, 1].axis('off')
ax[0, 1].set_title("bright")

# 3-3. 대비 이미지 (왼쪽 아래) -> ax[1,0] 유지
ax[1, 0].imshow(cv2.cvtColor(img_contrast, cv2.COLOR_BGR2RGB))
ax[1, 0].axis('off')
ax[1, 0].set_title("contrast")

# 3-4. 좌우반전 이미지 (오른쪽 아래)
# (방법 A: OpenCV 방식 사용 - 추천)
img_flip = cv2.flip(img, 1)
ax[1, 1].imshow(cv2.cvtColor(img_flip, cv2.COLOR_BGR2RGB))
# ax[1, 1].imshow(img_flip)

ax[1, 1].axis('off')
ax[1, 1].set_title("Flip")

# 4. 그림창 띄우기
plt.show()

# 5. 이미지 저장
cv2.imwrite("./2026_python/2026_data/captured_images/other_3_bright.jpg", img_bright)
cv2.imwrite("./2026_python/2026_data/captured_images/other_3_contrast.jpg", img_contrast)
cv2.imwrite("./2026_python/2026_data/captured_images/other_3_flip.jpg", img_flip)
print("이미지 저장 완료")