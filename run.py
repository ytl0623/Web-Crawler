import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def ratio(c, max_n, min_n):
    x,y,w,h = cv2.boundingRect(c)
    if( 1.0*w/h < max_n and 1.0*w/h > min_n):
        return True
    else:
        return False
        
# read from screen shot as gray image
img = cv2.imread("temp.png", cv2.IMREAD_GRAYSCALE)

# convert to only black and white
ret, img = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY_INV)

# for debug
img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# find all contours
(cnts, _) = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# find verification code block ratio in all contours
cnts = [c for c in cnts if  cv2.contourArea(c) > 1000 and ratio(c, 4.2, 4.1)]

# record the position
x, y, w, h = 0, 0, 0, 0
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img_color, (x, y), (x + w, y + h), (36,255,12), 5)

# cut out the code part
number_area = img[y:y+h, x:x+w]

# show code part image
#cv2.imshow("verify", number_area)
#cv2.waitKey()
#print("verify")

# tesseract ocr
text = pytesseract.image_to_string(number_area, config="--oem 3 --psm 7 digits")

# extract digit from string
print(text)
text = "".join([s for s in text if s.isdigit()])
print("132")
print(text)