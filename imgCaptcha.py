import pytesseract
from PIL import Image
import cv2 
import numpy as np
# Tesseract OCR의 실행 파일 경로를 직접 지정합니다.
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 이미지 파일의 경로를 지정합니다.
image_path = "Image.jpg"
image=cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 1)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)

cnts = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    if area < 50:
        cv2.drawContours(image, [c], -1, (0, 0, 0), -1)
kernel2 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
image = cv2.filter2D(image, -1, kernel2)
result = 255 - image
captcha_text = pytesseract.image_to_string(result)



# 추출한 텍스트를 출력합니다.
print(captcha_text)