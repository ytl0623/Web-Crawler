# https://ithelp.ithome.com.tw/questions/10209148

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://m.momoshop.com.tw/mymomo/login.momo") # 到登入頁面

driver.find_element(By.ID, 'memId').send_keys('0966106565') # 輸入帳號
driver.find_element(By.ID, 'passwd').send_keys('David890623') # 輸入密碼
driver.find_element(By.CLASS_NAME, 'login').click()  # 點擊

driver.get("https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=9113357&Area=search&mdiv=403&oid=1_1&cid=index&kw=9113357&mdiv=1099900000-bt_0_253_01-bt_0_253_01_P1_3_e1&ctype=B")

while True:
    try:
        localtime = time.strftime("20%y-%m-%d %H:%M:%S", time.localtime())
        buy = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located((By.ID, 'buy_yes'))) # 顯性等待
        buy.click() # 偵測到可以購買按鈕就點擊按鈕
        print (localtime, '可以購買!')
        break # 後面結帳部分就不寫囉
    except:
        print(localtime, "還不能購買! 重新整理!")
        driver.refresh() # 重整頁面

driver.find_element(By.ID, 'memId').send_keys('0966106565') # 輸入帳號
driver.find_element(By.ID, 'passwd_show').send_keys('David890623') # 輸入密碼
driver.find_element(By.CLASS_NAME, 'loginBtn').click()  # 點擊

print("Done")
input() # 不要把頁面關閉
driver.quit()






