import tkinter as tk
import os
import platform


# 開啟資料夾的函數
def open(path):
    os.startfile(path)


# 創建窗口
window = tk.Tk() 
window.title("快速啟動資料夾")
window.geometry("600x400")
window.configure(bg="lightblue")


button = tk.Button(window, text="魔獸資料夾", bg="lightgreen", font=("Arial", 14),
                     command=lambda: os.startfile(r"C:\Users\User\Documents\Warcraft III"))
button.grid(row=0, column=0, padx=20, pady=50)

button = tk.Button(window, text="世界RPG資料夾", bg="lightgreen", font=("Arial", 14),
                     command=lambda: open (r"C:\Users\User\Documents\Warcraft III\CustomMapData\TWRPG"))
button.grid(row=0, column=1, padx=20, pady=50) 

button = tk.Button(window, text="坦克資料夾", bg="lightgreen", font=("Arial", 14),
                     command=lambda: open(r"C:\Users\User\Documents\Warcraft III\CustomMapData\Random Ability Tank Defence"))
button.grid(row=0, column=2, padx=20, pady=50) 

button = tk.Button(window, text="開LANTW", bg="lightgreen", font=("Arial", 14),
                     command=lambda: open(r"E:\Lantw\LantwLauncher.exe"))
button.grid(row=1, column=0, padx=20, pady=50) 

button = tk.Button(window, text="開裝備查詢器", bg="lightgreen", font=("Arial", 14),
                     command=lambda: open(r"E:\QuickSearch_0.68p_fix1\QuickSearch.exe"))
button.grid(row=1, column=1, padx=20, pady=50) 

 


# button_f = tk.Button(window, text="測試", bg="lightgreen", font=("Arial", 14),
#                      command=lambda: open_folder(r"C:\Users\User\Documents\Warcraft III\CustomMapData\Random Ability Tank Defence"))
# button_f.grid(row=1, column=0, padx=20, pady=50)

# # 按鈕（指定各自位置的連結）
# button = tk.Button(window, text="世界RPG資料夾",bg="lightgreen", font=("Arial", 14),
#                    command=lambda: open_folder(r"C:\Users\User\Documents\Warcraft III\CustomMapData\TWRPG"))
# button.pack(side=tk.LEFT, padx=20, pady=50,)


# # 按鈕（指定各自位置的連結）
# button = tk.Button(window, text="魔獸資料夾",bg="lightgreen", font=("Arial", 14),
#                    command=lambda: open_folder(r"C:\Users\User\Documents\Warcraft III"))
# button.pack(side=tk.LEFT, padx=20, pady=50)
# #坦克
# button = tk.Button(window, text="坦克資料夾",bg="lightgreen", font=("Arial", 14),
#                    command=lambda: open_folder(r"C:\Users\User\Documents\Warcraft III\CustomMapData\Random Ability Tank Defence"))
# button.pack(side=tk.LEFT, padx=20, pady=50)

window.mainloop()


