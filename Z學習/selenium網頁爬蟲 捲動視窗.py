from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service       
from selenium.webdriver.chrome.options import Options 
import time
o=Options()
s = Service(r"E:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=o) 

driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")#訪問LinkedIn工作搜尋頁面

n=0
while n<5: #循環5次
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#捲動到最底部
    time.sleep(2) #等待2秒以確保頁面加載完成
    n+=1

titles = driver.find_elements(By.CLASS_NAME, "base-search-card__title")#找到所有工作標題元素

for title in titles:
    print(title.text)

driver.close() #關閉瀏覽器

