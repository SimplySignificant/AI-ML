import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        expression = entry.get()
        if not expression:
            messagebox.showwarning("Input", "Please enter an expression.")
            return

        result = eval(expression, {"__builtins__": {}}, {})
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid expression")


def clear_all():
    entry.delete(0, tk.END)


def add_text(value):
    entry.insert(tk.END, value)


root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 24), justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipadx=10, ipady=10)

button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

buttons = [
    ("7", lambda: add_text("7")),
    ("8", lambda: add_text("8")),
    ("9", lambda: add_text("9")),
    ("/", lambda: add_text("/")),
    ("4", lambda: add_text("4")),
    ("5", lambda: add_text("5")),
    ("6", lambda: add_text("6")),
    ("*", lambda: add_text("*")),
    ("1", lambda: add_text("1")),
    ("2", lambda: add_text("2")),
    ("3", lambda: add_text("3")),
    ("-", lambda: add_text("-")),
    ("0", lambda: add_text("0")),
    (".", lambda: add_text(".")),
    ("C", clear_all),
    ("+", lambda: add_text("+")),
]

row = 0
col = 0
for text, command in buttons:
    btn = tk.Button(
        button_frame, text=text, width=5, height=2, font=("Arial", 16), command=command
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

equals_btn = tk.Button(
    root, text="=", font=("Arial", 18), command=calculate, width=30, height=2
)
equals_btn.pack(padx=10, pady=(0, 10))

root.mainloop()
