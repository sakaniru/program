import tkinter as tk

def click(btn_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + btn_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    expr = entry.get()
    try:
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "錯誤")

root = tk.Tk()
root.title("簡易計算機")

entry = tk.Entry(root, width=16, font=('Arial', 24), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row = 1
col = 0
for btn in buttons:
    action = lambda x=btn: click(x) if x not in ['=', 'C'] else (calculate() if x == '=' else clear())
    tk.Button(root, text=btn, width=4, height=2, font=('Arial', 18), command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# root.mainloop()
