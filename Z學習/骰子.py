# import random

# k = random.randint(1, 6)

# if k == 1:
#     print("1")
# elif k == 2:
#     print("2")
# elif k == 3:
#     print("3")
# elif k == 4:
#     print("4")
# elif k == 5:
#     print("5")
# elif k == 6:
#     print("6")

import random
import time
import os

def clear():
    # 清除畫面，支援 Windows 和 Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_dice(k):
    dice_faces = {
        1: ("1"),
        2: ("2"),
        3: ("3"),
        4: ("4"),
        5: ("5"),
        6: ("6")
    }
    for line in dice_faces[k]:
        print(line)

# 模擬骰子滾動動畫
print(" 擲骰中...")
for i in range(5):  # 顯示5次變化
    k = random.randint(1, 6)
    clear()
    print("擲骰中...")
    draw_dice(k)
    time.sleep(0.2)
# 最後結果
clear()
print("結果：")
draw_dice(k)
# input("按任意鍵退出...")
