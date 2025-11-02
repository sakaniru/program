import pyautogui
import keyboard
import threading
import sys
import time

# ======= 左鍵控制 =======
holding = False  # 滑鼠左鍵狀態

def toggle_mouse(e):
    global holding
    holding = not holding
    if holding:
        pyautogui.mouseDown()
        print("滑鼠左鍵已按住")
    else:
        pyautogui.mouseUp()
        print("滑鼠左鍵已放開")

keyboard.on_press_key("B", toggle_mouse)

# ======= 自動按 F =======

auto_f = False  # 自動按 F 開關
interval = 0.02  # 每隔多少秒按一次 F

def toggle_auto_f(e):
    global auto_f
    auto_f = not auto_f
    if auto_f:
        print("開始自動按 F (代表現在會執行自動按F)")
    else:
        print("停止自動按 F (代表現在不會執行自動按F)")

keyboard.on_press_key("f6", toggle_auto_f)

# ======= 自動按 R =======
auto_r = False  # 自動按 R 開關
r_count = 0     # 計數器
r_max = 28      # 最大次數
def toggle_auto_r(e):
    global auto_r ,r_count
    auto_r = not auto_r
    if auto_r:
        r_count=0
        print("開始自動按 R")
    else:
        print("停止自動按 R")

keyboard.on_press_key("f3", toggle_auto_r)

def auto_press_r():
    global r_count,auto_r
    while True:
        if auto_r:
            keyboard.press_and_release("r")  # 模擬按一次 R
            r_count+=1
            if r_count>=r_max:
                auto_r=False
                print(f"已經到達{r_max}次數，停止")
        time.sleep(0.02)

def auto_press_f():
    while True:
        if auto_f:
            keyboard.press_and_release("f")  # 模擬按一次 f
        time.sleep(0.1)

# 啟動背景線程
threading.Thread(target=auto_press_f, daemon=True).start()


# 啟動背景線程
threading.Thread(target=auto_press_r, daemon=True).start()

print("按 B 切換滑鼠左鍵/停止自動按 R，按 F7 結束程式")



# 結束前確保滑鼠左鍵放開
if holding:
    pyautogui.mouseUp()
print("程式結束")
print("按 F7 鍵結束程式")
keyboard.wait("F7")  # 等待 F7
sys.exit(0)