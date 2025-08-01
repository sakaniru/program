import tkinter as tk
import random
def click():
    print("點擊了")
    
def off():
    print("關閉了")
    root.destroy()

def random_color():
    # 產生隨機顏色的十六進位字串，如 #A1B2C3
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

def change_btn_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = f'#{r:02x}{g:02x}{b:02x}'
    print("變更顏色為：", color)

    # 更改目標按鈕的背景色
    btn_target.config(bg=color)
    btnclick.config(bg=color)
    btn_change.config(bg=color)

def change():
    color = random_color()
    root.configure(bg=color)
    print(f"背景顏色變成: {color}")

# def on_resize(event):
#     # event.width, event.height 是視窗最新寬高
#     print(f"視窗大小變了：寬 {event.width} 高 {event.height}")


root=tk.Tk()
root.geometry("1000x800")
root.title("按鈕測試")
root.configure(bg="lightblue")

# 這是會被更改背景的按鈕
btn_target = tk.Button(root, text="我是按鈕", width=20, height=2)
btn_target.pack(pady=20)
# 這是觸發變色的按鈕
btn_color = tk.Button(root, text="改變其他按鈕的背景", command=change_btn_color)
btn_color.pack(pady=10)


btnclick=tk.Button(root,text="點我",command=click,width=10,height=5)
btnclick.pack(pady=100)
btn_change = tk.Button(root, text="隨機改背景色", command=change,width=10,height=5)
btn_change.pack(pady=100)
root.protocol("WM_DELETE_WINDOW",off)
# root.bind("<Configure>", on_resize)


root.mainloop()
