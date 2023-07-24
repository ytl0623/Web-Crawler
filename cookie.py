from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

# php
# driver = webdriver.Chrome()
# driver.get('http://demo.guru99.com/test/cookie/selenium_aut.php')

# driver.find_element(By.NAME, 'username').send_keys('abc123')
# driver.find_element(By.NAME, 'password').send_keys('123xyz')
# driver.find_element(By.NAME, 'submit').click()

# # storing the cookies
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
# driver.quit()

# driver = webdriver.Chrome()
# driver.get('http://demo.guru99.com/test/cookie/selenium_aut.php')

# # loading the stored cookies
# cookies = pickle.load(open("cookies.pkl", "rb"))

# for cookie in cookies:
    # print(cookie)
    # # adding the cookies to the session through webdriver instance
    # driver.add_cookie(cookie)

# driver.get('http://demo.guru99.com/test/cookie/selenium_cookie.php')
# driver.quit()

# book
# 可能是因為驗證碼，無法利用cookie自動登入
# driver = webdriver.Chrome()
# driver.get('https://cart.books.com.tw/member/login')

# driver.find_element(By.ID, 'login_id').send_keys('ytl0623') # 輸入帳號
# driver.find_element(By.ID, 'login_pswd').send_keys('David890623') # 輸入密碼
# driver.find_element(By.ID, 'captcha').send_keys(input()) # 輸入驗證碼(手動)
# driver.find_element(By.ID, 'books_login').click() # 點擊

# # storing the cookies
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
# driver.quit()

# driver = webdriver.Chrome()
# driver.get('https://cart.books.com.tw/member/login')

# # loading the stored cookies
# cookies = pickle.load(open("cookies.pkl", "rb"))

# for cookie in cookies:
    # print(cookie)
    # # adding the cookies to the session through webdriver instance
    # driver.add_cookie(cookie)
    
# driver.get('https://cart.books.com.tw/member/login')
# driver.quit()

# momo
# driver = webdriver.Chrome()
# driver.get('https://m.momoshop.com.tw/mymomo/login.momo')

# driver.find_element(By.ID, 'memId').send_keys('0966106565') # 輸入帳號
# driver.find_element(By.ID, 'passwd').send_keys('David890623') # 輸入密碼
# driver.find_element(By.CLASS_NAME, 'login').click()  # 點擊

# # storing the cookies
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
# driver.quit()

# driver = webdriver.Chrome()
# driver.get('https://m.momoshop.com.tw/mymomo/login.momo')

# # loading the stored cookies
# cookies = pickle.load(open("cookies.pkl", "rb"))

# for cookie in cookies:
    # print(cookie)
    # # adding the cookies to the session through webdriver instance
    # driver.add_cookie(cookie)
    
# driver.get('https://m.momoshop.com.tw/mymomo/login.momo')
# driver.quit()

# php cookie log
{'domain': 'demo.guru99.com', 'expiry': 1676434837, 'httpOnly': False, 'name': 'geo-location', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '{"country":"TW","region":"CYI"}'}
{'domain': '.guru99.com', 'expiry': 1707884437, 'httpOnly': False, 'name': 'FCNEC', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%5B%5B%22AKsRol8S0KMiwRFUK7wa-fG6jXEZqHUYmSRYfB7nTvybe1zuZ1Gz_YsBGbkewiUeYYvA2nOPr_wNvyJYApUMSotfCQTyZQpByFUOWIo8N6JKDEcscP3q9FLwH9LtzOP2GHBgGJsa1wjoi4U3BIW9SM_jOEgFP8lhSg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D'}
{'domain': '.guru99.com', 'expiry': 1710044436, 'httpOnly': False, 'name': 'cto_bundle', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1vck419qa0dMWFFNWTlJS2FVMUFON1p6bDJhMnFuaWpoJTJGSVl4amNndVZrVGdqZlhJd2ZUWlFGY3RnWlVKQm5QekhQVVdwVTNPM1h0V2ROeFNJZzEyakVzbW8zQks3UWo5VHNhTVhGWFZ6TFI5aXBKYmF5RkVCa3gza0U0TWZkWE1tZVFReHFhZjZXVm9ncUU2NkRFdU9zS3ZrdyUzRCUzRA'}
{'domain': '.guru99.com', 'expiry': 1676953233, 'httpOnly': False, 'name': 'panoramaId', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '60e60f12bd5d47205a932fa0455d16d53938f3d46bef876ca8fe099760de22aa'}
{'domain': '.guru99.com', 'expiry': 1710044432, 'httpOnly': False, 'name': '__gads', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ID=ed151d8028525dc7:T=1676348432:S=ALNI_MbX7OLIOBpXGwkV6h3r_KTMr-3NPg'}
{'domain': 'demo.guru99.com', 'expiry': 1710044437, 'httpOnly': False, 'name': 'usprivacy', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1---'}
{'domain': '.guru99.com', 'expiry': 1699676435, 'httpOnly': False, 'name': '_cc_id', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'f9cb1f6a44c2d975ac96fc889ea0493a'}
{'domain': '.guru99.com', 'expiry': 1676953233, 'httpOnly': False, 'name': 'panoramaId_expiry', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1676953233105'}
{'domain': '.guru99.com', 'expiry': 1676348495, 'httpOnly': False, 'name': '_gat_gtag_UA_1248015_24', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}
{'domain': '.guru99.com', 'expiry': 1676348445, 'httpOnly': False, 'name': 'lotame_domain_check', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'guru99.com'}
{'domain': 'demo.guru99.com', 'httpOnly': False, 'name': 'Selenium', 'path': '/test/cookie', 'sameSite': 'Lax', 'secure': False, 'value': 'abc123'}
{'domain': '.guru99.com', 'expiry': 1676434837, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.2.88857829.1676348435'}
{'domain': 'demo.guru99.com', 'expiry': 1678940437, 'httpOnly': False, 'name': '_pbjs_userid_consent_data', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '6683316680106290'}
{'domain': '.guru99.com', 'expiry': 1710908437, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.2.78633851.1676348435'}
{'domain': '.guru99.com', 'expiry': 1710044432, 'httpOnly': False, 'name': '__gpi', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'UID=00000bc1906c6a3a:T=1676348432:RT=1676348432:S=ALNI_May45_dhrUWypIG12mCJvhnz__2Vw'}
{'domain': '.guru99.com', 'expiry': 1707884434, 'httpOnly': False, 'name': '_sharedid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '216b0aa4-95bc-467e-889d-17c36323c28a'}

# book cookie log
{'domain': '.books.com.tw', 'expiry': 1676348675, 'httpOnly': False, 'name': '_gali', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'books_login'}
{'domain': '.books.com.tw', 'expiry': 1710044635, 'httpOnly': False, 'name': '__gpi', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'UID=00000bc18fe6c2bb:T=1676348635:RT=1676348635:S=ALNI_MYn7YXfKc9cAW4a7u3lJE7HsXO0UA'}
{'domain': '.books.com.tw', 'expiry': 1710044635, 'httpOnly': False, 'name': '__gads', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ID=026665d468e2bc33:T=1676348635:S=ALNI_MbpwvZX4kK2wS1uqb1X7n9yhOJdkQ'}
{'domain': '.books.com.tw', 'expiry': 1684124645, 'httpOnly': False, 'name': '_fbp', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'fb.2.1676348638018.1011865896'}
{'domain': '.books.com.tw', 'expiry': 1676348697, 'httpOnly': False, 'name': '_dc_gtm_UA-4860506-1', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '1'}
{'domain': '.cart.books.com.tw', 'expiry': 1676350437, 'httpOnly': False, 'name': '__lt__sid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '8c590cd3-468110e7'}
{'domain': '.cart.books.com.tw', 'expiry': 1710908637, 'httpOnly': False, 'name': '__lt__cid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '59c88ade-5189-4fe0-8b56-ce326bb18c3b'}
{'domain': '.books.com.tw', 'expiry': 1710908637, 'httpOnly': False, 'name': '_ga_P8GKGRYDVG', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GS1.1.1676348637.1.0.1676348637.60.0.0'}
{'domain': 'cart.books.com.tw', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '6pe4okg4hbnmmjvndbgle1bkg2'}
{'domain': '.books.com.tw', 'expiry': 1676348937, 'httpOnly': True, 'name': 'bt', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'rq1yvt'}
{'domain': '.books.com.tw', 'expiry': 1710908637, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'GA1.3.1036453157.1676348638'}
{'domain': 'cart.books.com.tw', 'httpOnly': True, 'name': 'ukk', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '72e2d148566b2ed27300965d938480874c81debc'}
{'domain': '.books.com.tw', 'expiry': 1676435037, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'GA1.3.437491658.1676348638'}
{'domain': '.books.com.tw', 'expiry': 1710908637, 'httpOnly': True, 'name': 'bid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '63eb0cd922a44'}
{'domain': '.books.com.tw', 'expiry': 1676350437, 'httpOnly': True, 'name': 'ssid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '63eb0cd922a44.1676348633'}
{'domain': '.books.com.tw', 'expiry': 1684124637, 'httpOnly': False, 'name': '_gcl_au', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1.1.1478129856.1676348638'}

# momo cookie log
{'domain': 'www.momoshop.com.tw', 'httpOnly': True, 'name': 'wsf_web', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'wsf_web_c_25'}















