import tkinter as tk
from tkinter import font as tkFont

#Functions for calculator
def append_to_expression(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def clear_display():
    display.delete(0, tk.END)

#Main window setup
root = tk.Tk()
root.title("Calculator")
root.geometry("300x450")
root.resizable(False, False)

display = tk.Entry(root, font=('Helvetica', 20), bd=10, insertwidth=1, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Calculator Buttons
button_font = tkFont.Font(family="Helvetica", size=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3), ('=', 4, 2),
    ('C', 4, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=button_font, command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=button_font, command=clear_display)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=button_font, command=lambda t=text: append_to_expression(t))
    btn.grid(row=row, column=col, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
    for j in range(4):
        root.grid_columnconfigure(j, weight=1)

root.mainloop()
