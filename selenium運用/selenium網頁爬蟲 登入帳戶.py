#網頁爬蟲 爬取 LeetCode 個人刷題紀錄 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
o = Options()
s = Service(r"E:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=o)
driver.get("https://leetcode.com/accounts/login/")  # 訪問LeetCode登入頁面



