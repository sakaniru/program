# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

# options=Options()
# Service=Service("E:\chromedriver-win64\chromedriver-win64")
# driver=webdriver.Chrome(options=options)
# # driver.set_window_size(800, 600)#自訂大小
# driver.maximize_window()#最大化
# driver.get("https://www.google.com/")
# driver.save_screenshot("google螢幕截圖測試.png")#網頁截圖
# driver.get("https://www.ntu.edu.tw/")
# driver.save_screenshot("台大截圖.png")
# driver.close()

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument("incognito")#無痕模式
# options.add_argument("--window-size=600,800")#自訂大小
# options.add_argument("--start-maximized")#最大化開始
service=Service("E:\\chromedriver-win64\\chromedriver.exe")#指定路徑要用\\隔開
driver=webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
driver.save_screenshot("google截圖測試.png")
driver.close()