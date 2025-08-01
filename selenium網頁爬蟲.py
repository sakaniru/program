from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service       
from selenium.webdriver.chrome.options import Options 
o=Options()
s = Service(r"E:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=o) 

driver.get("https://www.ptt.cc/bbs/Stock/index9099.html")

# print(driver.page_source)#原始碼
tags = driver.find_elements(By.CLASS_NAME,"title")
for tag in tags:
    print(tag.text)

    
link=driver.find_element(By.LINK_TEXT,"‹ 上頁").click() #上一頁
tags = driver.find_elements(By.CLASS_NAME,"title")
for tag in tags:
    print(tag.text)

driver.close() #關閉瀏覽器