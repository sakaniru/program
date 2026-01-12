import tkinter as tk
from tkinter import messagebox
import os
import time
import threading
from datetime import datetime, timedelta

shutdown_time = None
countdown_running = False

def schedule_by_minutes():
    global shutdown_time, countdown_running
    try:
        minutes = int(entry_minutes.get())
        if minutes <= 0:
            raise ValueError

        shutdown_time = datetime.now() + timedelta(minutes=minutes)
        seconds = minutes * 60
        os.system(f"shutdown -s -t {seconds}")

        countdown_running = True
        messagebox.showinfo("設定成功", f"{minutes} 分鐘後將自動關機")

    except ValueError:
        messagebox.showerror("錯誤", "請輸入正整數分鐘")

def schedule_by_time():
    global shutdown_time, countdown_running
    try:
        hour = int(entry_hour.get())
        minute = int(entry_minute.get())

        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError

        now = datetime.now()
        shutdown_time = now.replace(hour=hour, minute=minute, second=0)

        if shutdown_time <= now:
            shutdown_time += timedelta(days=1)

        seconds = int((shutdown_time - now).total_seconds())
        os.system(f"shutdown -s -t {seconds}")

        countdown_running = True
        messagebox.showinfo(
            "設定成功",
            f"將於 {shutdown_time.strftime('%H:%M')} 自動關機"
        )

    except ValueError:
        messagebox.showerror("錯誤", "請輸入正確時間")

def cancel_shutdown():
    global countdown_running
    os.system("shutdown -a")
    countdown_running = False
    label_countdown.config(text="已取消關機")

def update_countdown():
    while True:
        if countdown_running and shutdown_time:
            remaining = shutdown_time - datetime.now()
            if remaining.total_seconds() <= 0:
                break

            mins, secs = divmod(int(remaining.total_seconds()), 60)
            hours, mins = divmod(mins, 60)
            label_countdown.config(
                text=f"剩餘時間：{hours:02d}:{mins:02d}:{secs:02d}"
            )
        time.sleep(1)

# ===== GUI =====
root = tk.Tk()
root.title("智慧自動關機")
root.geometry("360x320")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

font_main = ("Microsoft JhengHei", 10)
fg = "#ffffff"
bg = "#1e1e1e"
btn_bg = "#333333"

tk.Label(root, text="🕒 幾分鐘後關機", bg=bg, fg=fg, font=font_main).pack(pady=5)
entry_minutes = tk.Entry(root, justify="center", font=font_main)
entry_minutes.insert(0, "30")
entry_minutes.pack()
tk.Button(root, text="設定", command=schedule_by_minutes, bg=btn_bg, fg=fg).pack(pady=5)

tk.Label(root, text="⏰ 指定時間關機（24小時制）", bg=bg, fg=fg, font=font_main).pack(pady=5)
frame_time = tk.Frame(root, bg=bg)
frame_time.pack()

entry_hour = tk.Entry(frame_time, width=5, justify="center")
entry_hour.insert(0, "23")
entry_hour.pack(side="left", padx=5)

tk.Label(frame_time, text=":", bg=bg, fg=fg).pack(side="left")

entry_minute = tk.Entry(frame_time, width=5, justify="center")
entry_minute.insert(0, "30")
entry_minute.pack(side="left", padx=5)

tk.Button(root, text="設定時間關機", command=schedule_by_time, bg=btn_bg, fg=fg).pack(pady=5)

label_countdown = tk.Label(root, text="尚未設定", bg=bg, fg="#00ffcc", font=font_main)
label_countdown.pack(pady=10)

tk.Button(root, text="❌ 取消關機", command=cancel_shutdown, bg="#662222", fg=fg).pack(pady=5)

threading.Thread(target=update_countdown, daemon=True).start()

root.mainloop()
