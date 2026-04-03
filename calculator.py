import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%", "√",]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray = "#d4d4d2"
color_black = "#1c1c1c"
color_dark_gray = "#505050"
color_orange = "#ff9500"
color_white = "#ffffff"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black, 
                      foreground=color_white, anchor="e", width=column_count) 
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value =     button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), 
                                width=column_count-1, height=1,
                                command=lambda value=value: button_click(value))
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        button.grid(row=row+1, column=column)

frame.pack()

A = 0
operator = None
B = None

def clear_all():
    global A, operator, B
    A = 0
    operator = None
    B = None

def remove_zero_decimal(num):
    if num == int(num):
        num = int(num)
    return str(num)

def button_click(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                num_A = float(A)
                num_B = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(num_A + num_B)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(num_A - num_B)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(num_A * num_B)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(num_A / num_B)

                clear_all()
        elif value in "÷×-+":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
        elif value == "√":
            result = float(label["text"]) ** 0.5
            label["text"] = remove_zero_decimal(result)
    else: 
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value
        

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
