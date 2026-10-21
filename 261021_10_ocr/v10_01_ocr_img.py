import pytesseract          # OCR 사용
from PIL import Image  #이미지 처리 도구
import os

# 1 Tesseract 실행 파일 경로 지정
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# 2 이미지 불러오기
image = Image.open("261021_10_ocr/img.jpg")
# image = Image.open("261021_10_ocr/input.jpg")
# image = Image.open("261021_10_ocr/output_img.jpg")

# 3 OCR 수행
results = pytesseract.image_to_string(
    image,
    lang='eng+kor'
)

# 4 결과 출럭
print(f"OCR 실행 결과 : {results}")



# OCR 실행 결과 : This is a lot of 12 point text to test the
# ocr code and see if it works on all types
# of file format.

# The quick brown dog jumped over the
# lazy fox. The quick brown dog jumped
# over the lazy fox. The quick brown dog
# jumped over the lazy fox. The quick
# brown dog jumped over the lazy fox.


# OCR 실행 결과 : LARANASKIN

# 이수진

# 팀장 / 제 품 개발팀

# +123-456-7890
# hello@reallygreatsite.com
# 123 Anywhere St., Any City, ST 12345