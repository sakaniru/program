from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
from collections import deque

# ---------- 設定 ----------
WEBHOOK_URL = "https://discord.com/api/webhooks/1419294065937092660/lyhspPbTqkunidABckrpYj-trsmYgfOfFTE8zAkbrl2bqK5iOjorrb27I01D_14rAK9m"
URL = "https://gamebanana.com/mods/cats/29524?subcat=skins"  # Skins 子分類
LAST_FILE = "last_update.txt"
MAX_ITEMS = 10   # 每次最多抓取最新 10 個
MAX_HISTORY = 200  # 最多保留 200 筆歷史
EXCLUDE_TITLES = {"Add Mod", "Overview", "Skins", "Mods"}  # 過濾導航/分類

# ---------- 函數 ----------
def get_latest_skins():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    # 顯式等待 mod 列表出現
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/mods/']"))
        )
    except:
        print("等待 mod 列表載入超時")
        driver.quit()
        return []

    mods = driver.find_elements(By.CSS_SELECTOR, "a[href*='/mods/']")
    results = []
    seen = set()
    for mod in mods:
        title = mod.text.strip()
        link = mod.get_attribute("href")
        if title and link and title not in seen and title not in EXCLUDE_TITLES:
            results.append((title, link))
            seen.add(title)
        if len(results) >= MAX_ITEMS:  # 只抓最新 MAX_ITEMS 個
            break

    driver.quit()
    print(f"抓到 {len(results)} 個最新 Skins")
    return results

def send_discord(title, link):
    data = {"content": f"🔔 GameBanana 最新 Skins！\n**{title}**\n{link}"}
    requests.post(WEBHOOK_URL, json=data)

def read_last_titles():
    if not os.path.exists(LAST_FILE):
        return deque(maxlen=MAX_HISTORY)
    with open(LAST_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
        return deque(lines, maxlen=MAX_HISTORY)

def write_last_titles(records):
    with open(LAST_FILE, "w", encoding="utf-8") as f:
        for r in records:
            f.write(r + "\n")

# ---------- 主程式 ----------
def main():
    latest_skins = get_latest_skins()
    if not latest_skins:
        print("未找到任何 Skins")
        return

    last_titles = read_last_titles()
    new_skins = []
    for title, link in latest_skins:
        key = f"{title}|{link}"
        if key not in last_titles:
            new_skins.append((title, link))
            last_titles.append(key)  # 加入歷史紀錄（自動維持 200 筆）

    if new_skins:
        for title, link in reversed(new_skins):  # 依順序推送
            send_discord(title, link)
            print(f"已推送: {title}")

        # 更新 last_update.txt（最多保留 200 筆）
        write_last_titles(last_titles)
    else:
        print("沒有新更新的 Skins。")

if __name__ == "__main__":
    main()
