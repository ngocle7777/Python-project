# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import font
import math

# --- CÁC HÀM XỬ LÝ TOÁN HỌC AN TOÀN ---

# Định nghĩa các hàm wrapper để tính toán an toàn, đặc biệt là chuyển đổi độ sang radian cho các hàm lượng giác
def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    # Xử lý trường hợp tan(90), tan(270),...
    if x % 180 == 90:
        return float('inf') # Trả về vô cực
    return math.tan(math.radians(x))

# Tạo một dictionary chứa các hàm và hằng số an toàn để sử dụng với eval()
# Điều này ngăn chặn việc thực thi các mã độc hại.
SAFE_EVAL_DICT = {
    "sin": sin_deg,
    "cos": cos_deg,
    "tan": tan_deg,
    "sqrt": math.sqrt,
    "log": math.log10, # log cơ số 10
    "ln": math.log,    # log cơ số e
    "factorial": math.factorial,
    "pi": math.pi,
    "e": math.e,
    "pow": pow,
}

# --- CÁC HÀM XỬ LÝ GIAO DIỆN ---

def on_button_click(char):
    """
    Hàm này được gọi khi người dùng nhấn một nút.
    Nó sẽ thêm ký tự hoặc chuỗi tương ứng vào ô hiển thị.
    """
    current_text = display.get()
    # Xóa nội dung "Lỗi" hoặc "0" ban đầu khi người dùng bắt đầu nhập
    if current_text == "Lỗi" or (current_text == "0" and char not in ".(+-×÷"):
        display.delete(0, tk.END)
    display.insert(tk.END, str(char))

def calculate():
    """
    Hàm này được gọi khi người dùng nhấn nút "=".
    Nó sẽ lấy biểu thức từ ô hiển thị, thay thế các ký tự cho thân thiện
    với Python, và tính toán kết quả một cách an toàn bằng eval().
    """
    try:
        expression = display.get().replace("÷", "/").replace("×", "*").replace("√", "sqrt").replace("π", "pi")
        
        # Xử lý giai thừa (x!) và lũy thừa (x^y)
        expression = expression.replace("!", "factorial")
        expression = expression.replace("^", "**")

        # Tính toán an toàn với eval
        result = eval(expression, {"__builtins__": None}, SAFE_EVAL_DICT)
        
        display.delete(0, tk.END)
        # Hiển thị số nguyên nếu kết quả không có phần thập phân
        if result == int(result):
            display.insert(0, str(int(result)))
        else:
            # Làm tròn kết quả để tránh các số thập phân quá dài
            display.insert(0, str(round(result, 10)))
    except Exception as e:
        # Nếu có lỗi, hiển thị "Lỗi"
        display.delete(0, tk.END)
        display.insert(0, "Lỗi")
        print(f"Lỗi tính toán: {e}") # In lỗi ra console để debug

def clear_display():
    """
    Hàm này được gọi khi người dùng nhấn nút "C".
    Nó sẽ xóa toàn bộ nội dung và đặt lại là "0".
    """
    display.delete(0, tk.END)
    display.insert(0, "0")

def delete_char():
    """
    Hàm này xóa ký tự cuối cùng trong ô hiển thị (chức năng Backspace).
    """
    current_text = display.get()
    if current_text != "Lỗi" and len(current_text) > 0:
        new_text = current_text[:-1]
        display.delete(0, tk.END)
        if not new_text:
            display.insert(0, "0")
        else:
            display.insert(0, new_text)

# --- THIẾT LẬP GIAO DIỆN ---

window = tk.Tk()
window.title("Máy Tính Khoa Học")
window.geometry("450x650")
window.minsize(450, 650)
window.configure(bg="#1c1c1c")

window.grid_rowconfigure(0, weight=2)
window.grid_rowconfigure(1, weight=5)
window.grid_columnconfigure(0, weight=1)

display_font = font.Font(family="Helvetica", size=48)
button_font = font.Font(family="Helvetica", size=16)

display = tk.Entry(
    window, font=display_font, bg="#1c1c1c", fg="white",
    borderwidth=0, justify="right", relief="flat"
)
display.grid(row=0, column=0, sticky="nsew", padx=20, pady=(20, 0))
display.insert(0, "0")

button_frame = tk.Frame(window, bg="#1c1c1c")
button_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

for i in range(5): button_frame.grid_columnconfigure(i, weight=1)
for i in range(6): button_frame.grid_rowconfigure(i, weight=1)

buttons_layout = [
    # text, command, row, col, [colspan], [bg_color], [fg_color]
    ('sin', lambda: on_button_click('sin('), 0, 0, 1, '#2a2a2a'),
    ('cos', lambda: on_button_click('cos('), 0, 1, 1, '#2a2a2a'),
    ('tan', lambda: on_button_click('tan('), 0, 2, 1, '#2a2a2a'),
    ('DEL', delete_char, 0, 3, 1, '#a6a6a6', 'black'),
    ('C', clear_display, 0, 4, 1, '#a6a6a6', 'black'),
    
    ('log', lambda: on_button_click('log('), 1, 0, 1, '#2a2a2a'),
    ('ln', lambda: on_button_click('ln('), 1, 1, 1, '#2a2a2a'),
    ('x²', lambda: on_button_click('**2'), 1, 2, 1, '#2a2a2a'),
    ('xʸ', lambda: on_button_click('^'), 1, 3, 1, '#2a2a2a'),
    ('√', lambda: on_button_click('√('), 1, 4, 1, '#2a2a2a'),

    ('(', lambda: on_button_click('('), 2, 0, 1, '#2a2a2a'),
    (')', lambda: on_button_click(')'), 2, 1, 1, '#2a2a2a'),
    ('x!', lambda: on_button_click('!'), 2, 2, 1, '#2a2a2a'),
    ('π', lambda: on_button_click('π'), 2, 3, 1, '#2a2a2a'),
    ('÷', lambda: on_button_click('÷'), 2, 4, 1, '#ff9500'),

    ('7', lambda: on_button_click('7'), 3, 0),
    ('8', lambda: on_button_click('8'), 3, 1),
    ('9', lambda: on_button_click('9'), 3, 2),
    ('×', lambda: on_button_click('×'), 3, 3, 1, '#ff9500'),
    ('-', lambda: on_button_click('-'), 3, 4, 1, '#ff9500'),

    ('4', lambda: on_button_click('4'), 4, 0),
    ('5', lambda: on_button_click('5'), 4, 1),
    ('6', lambda: on_button_click('6'), 4, 2),
    ('+', lambda: on_button_click('+'), 4, 3, 1, '#ff9500'),
    ('=', calculate, 4, 4, 1, '#ff9500', 'white', 2), # rowspan=2

    ('1', lambda: on_button_click('1'), 5, 0),
    ('2', lambda: on_button_click('2'), 5, 1),
    ('3', lambda: on_button_click('3'), 5, 2),
    ('0', lambda: on_button_click('0'), 6, 0, 2),
    ('.', lambda: on_button_click('.'), 6, 2),
]

for config in buttons_layout:
    text, cmd, row, col = config[:4]
    colspan = config[4] if len(config) > 4 else 1
    bg = config[5] if len(config) > 5 else '#333333'
    fg = config[6] if len(config) > 6 else 'white'
    rowspan = config[7] if len(config) > 7 else 1
    
    button = tk.Button(
        button_frame, text=text, font=button_font, bg=bg, fg=fg,
        borderwidth=0, relief="flat", activebackground="#555555",
        activeforeground="white", command=cmd
    )
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=5, pady=5)

window.mainloop()

