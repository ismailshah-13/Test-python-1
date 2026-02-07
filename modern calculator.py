import tkinter as tk

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = "Error" if num2 == 0 else num1 / num2

        result_label.config(text=str(result))

    except ValueError:
        result_label.config(text="Invalid Input")

# ---------------- Window ----------------
window = tk.Tk()
window.title("Modern Calculator")
window.geometry("320x420")
window.configure(bg="#1E1E1E")
window.resizable(False, False)

# ---------------- Display ----------------
display_frame = tk.Frame(window, bg="#1E1E1E")
display_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

tk.Label(
    display_frame,
    text="Result",
    fg="#AAAAAA",
    bg="#1E1E1E",
    anchor="e"
).grid(row=0, column=0, sticky="e")

result_label = tk.Label(
    display_frame,
    text="0",
    fg="white",
    bg="#1E1E1E",
    font=("Segoe UI", 28, "bold"),
    anchor="e",
    width=12
)
result_label.grid(row=1, column=0, pady=5)

# ---------------- Inputs ----------------
entry1 = tk.Entry(
    window,
    font=("Segoe UI", 16),
    justify="right",
    bd=0,
    bg="#2B2B2B",
    fg="white",
    insertbackground="white"
)
entry1.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="we")

entry2 = tk.Entry(
    window,
    font=("Segoe UI", 16),
    justify="right",
    bd=0,
    bg="#2B2B2B",
    fg="white",
    insertbackground="white"
)
entry2.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="we")

# ---------------- Buttons ----------------
btn_style = {
    "font": ("Segoe UI", 14, "bold"),
    "bd": 0,
    "width": 6,
    "height": 2
}

op_color = "#FF9500"
num_color = "#3A3A3A"
text_color = "white"

tk.Button(window, text="+", bg=op_color, fg="white",
          command=lambda: calculate("+"), **btn_style).grid(row=3, column=0, padx=8, pady=8)

tk.Button(window, text="-", bg=op_color, fg="white",
          command=lambda: calculate("-"), **btn_style).grid(row=3, column=1, padx=8, pady=8)

tk.Button(window, text="×", bg=num_color, fg=text_color,
          command=lambda: calculate("*"), **btn_style).grid(row=4, column=0, padx=8, pady=8)

tk.Button(window, text="÷", bg=num_color, fg=text_color,
          command=lambda: calculate("/"), **btn_style).grid(row=4, column=1, padx=8, pady=8)

# ---------------- Layout control ----------------
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()
