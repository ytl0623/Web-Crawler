# from selenium import webdriver

# option = webdriver.ChromeOptions()
# option.add_argument(r'--user-data-dir=C:\Users\ytlWin\AppData\Local\Google\Chrome\User Data\Profile 6')
# driver = webdriver.Chrome(option)

# # driver.get("https://cart.books.com.tw/member/login")
# driver.get("https://www.google.com.tw/")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--user-data-dir=C:\\Users\\ytlWin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 6")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")