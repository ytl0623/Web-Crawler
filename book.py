# https://ithelp.ithome.com.tw/questions/10209148

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import cv2
import ddddocr
import os

# options = webdriver.ChromeOptions()
# # options.add_argument(r'--user-data-dir=C:\Users\ytlWin\AppData\Local\Google\Chrome\User Data')
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
#
# driver.get("https://cart.books.com.tw/member/login") # 到登入頁面
# driver.save_screenshot("temp.png")
#
# driver.find_element(By.ID, 'login_id').send_keys('ytl0623') # 輸入帳號
# driver.find_element(By.ID, 'login_pswd').send_keys('David890623') # 輸入密碼
# driver.find_element(By.ID, 'captcha').send_keys(input()) # 輸入驗證碼(手動)
# driver.find_element(By.ID, 'books_login').click() # 點擊
#
#
# input()
#
#
# driver.get("https://www.books.com.tw/products/N001400260") # 商品網址
#
# while True:
#     try:
#         localtime = time.strftime("20%y-%m-%d %H:%M:%S", time.localtime())
#         buy = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_neweasycart'))) # 顯性等待 # 確認CLASS_NAME
#         buy.click() # 偵測到可以購買按鈕就點擊按鈕
#         print(localtime, '可以購買!')
#         break
#     except:
#         print(localtime, "還不能購買! 重新整理!")
#         driver.refresh() # 重整頁面
#
# driver.find_element(By.ID, 'login_id').send_keys('ytl0623') # 輸入帳號
# driver.find_element(By.ID, 'login_pswd').send_keys('David890623') # 輸入密碼
# driver.find_element(By.ID, 'captcha').send_keys(input()) # 輸入驗證碼(手動)
# driver.find_element(By.ID, 'books_login').click() # 點擊
#
# print("Done")
# input() # 不要把頁面關閉
# driver.quit()

# read from screen shot as gray image
img = cv2.imread("temp.png")

# 裁切區域的 x 與 y 座標（左上角）
x = 1080
y = 310

# 裁切區域的長度與寬度
w = 200
h = 70

# 裁切圖片
crop_img = img[y:y+h, x:x+w]
cv2.imwrite("crop.png", crop_img)

ocr = ddddocr.DdddOcr(show_ad=False, beta=True)
image_file = 'crop.png'
if os.path.exists(image_file):
  with open(image_file, 'rb') as f:
    image_bytes = f.read()
  res = ocr.classification(image_bytes)
  print(res)















