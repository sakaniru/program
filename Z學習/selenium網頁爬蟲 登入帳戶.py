#網頁爬蟲 登入google帳戶
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
o = Options()
s = Service(r"E:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=o)
driver.get("https://accounts.google.com/signin")  # 訪問Google登入頁面
# 等待頁面加載
time.sleep(2)
# 找到帳號和密碼輸入框
username_input = driver.find_element(By.ID, "identifierId")
password_input = driver.find_element(By.NAME, "password")
# 輸入帳號和密碼
username_input.send_keys("your_email@example.com")
password_input.send_keys("your_password")
# 找到登入按鈕並點擊
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
# 等待登入完成
time.sleep(5)  # 根據需要調整等待時間
# 確認登入成功
if "myaccount" in driver.current_url:
    print("登入成功！")
else:
    print("登入失敗，請檢查帳號或密碼。")


# 關閉瀏覽器
# driver.close()  # 關閉瀏覽器
# 注意：請將 "your_email@example.com" 和 "your_password" 替換為您的Google帳號和密碼。
# 此代碼僅供學習和測試使用，請遵守Google的使用條款和隱私政策。
# 確保在使用自動化工具時遵守網站的使用條款。
