import pyautogui
import keyboard
import time

# --- 設定區 ---
# 滑鼠移動速度 (秒)
move_speed = 0.5 
# -------------

# 用字典來儲存三個獨立的座標，預設為 None (空)
saved_positions = {
    1: None,
    2: None,
    3: None
}

def save_point(slot_num):
    """
    通用函式：用來記錄座標到指定的插槽 (1, 2, 或 3)
    """
    global saved_positions
    x, y = pyautogui.position()
    saved_positions[slot_num] = (x, y)
    print(f"✅ [紀錄] 位置 {slot_num} 已更新為: ({x}, {y})")

def execute_point(slot_num):
    """
    通用函式：用來執行指定插槽的移動與點擊
    """
    target = saved_positions[slot_num]
    
    # 檢查該位置是否已經設定過
    if target is None:
        print(f"❌ [錯誤] 位置 {slot_num} 尚未設定！請先將滑鼠移好並按 F{slot_num} 紀錄。")
        return

    x, y = target
    print(f"▶️ [執行] 前往位置 {slot_num}: ({x}, {y})...")
    
    # 移動並點擊
    pyautogui.moveTo(x, y, duration=move_speed)
    pyautogui.click()
    print(f"✨ 位置 {slot_num} 點擊完成")

# --- 設定熱鍵 ---
# args=(1,) 代表把 1 這個數字傳進函式裡

# 紀錄鍵：F1, F2, F3
keyboard.add_hotkey('f1', save_point, args=(1,))
keyboard.add_hotkey('f2', save_point, args=(2,))
keyboard.add_hotkey('f3', save_point, args=(3,))

# 執行鍵：鍵盤上方的數字 1, 2, 3
keyboard.add_hotkey('1', execute_point, args=(1,))
keyboard.add_hotkey('2', execute_point, args=(2,))
keyboard.add_hotkey('3', execute_point, args=(3,))

print("=== 多點獨立控制程式已啟動 ===")
print("設定座標：移動滑鼠，分別按 [F1]、[F2]、[F3] 來記錄三個不同位置")
print("執行點擊：分別按數字鍵 [1]、[2]、[3] 來執行對應的點擊")
print("離開程式：按 [Esc] 或 [Ctrl+C]")

try:
    # 讓程式保持運行，直到按下 Esc
    keyboard.wait('esc')
    print("\n使用者按下了 Esc，程式正常結束。")
except KeyboardInterrupt:
    # 這裡捕捉 Ctrl+C 的訊號，防止報錯
    print("\n\n使用者強制中斷 (Ctrl+C)，程式結束。")
finally:
    keyboard.unhook_all()