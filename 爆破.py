import pyautogui
import time
import threading
import tkinter as tk

def start_program():
    # 取得使用者輸入的固定前4位數字和後2位數字
    prefix = prefix_entry.get()
    suffix = suffix_entry.get()

    # 取得使用者輸入的輸入框座標
    input_box_x = int(input_box_x_entry.get())
    input_box_y = int(input_box_y_entry.get())

    # 取得使用者輸入的送出按鈕座標
    submit_button_x = int(submit_button_x_entry.get())
    submit_button_y = int(submit_button_y_entry.get())

    # 取得使用者輸入的休息時間和輸入時間
    rest_time = int(rest_time_entry.get())
    input_time = int(input_time_entry.get())

    # 開始循環輸入數字和點擊送出按鈕
    middle_number_start = int(middle_number_start_entry.get())
    middle_number_end = int(middle_number_end_entry.get())

    for number in range(middle_number_start, middle_number_end + 1):
        # 格式化中間的四位數字為四位數的字符串
        middle_number_str = "{:04d}".format(number)

        # 構建完整的數字
        full_number_str = prefix + middle_number_str + suffix

        # 將焦點設定到輸入框並輸入數字
        # 先點擊輸入框兩次
        pyautogui.click(input_box_x, input_box_y)
        pyautogui.click(input_box_x, input_box_y)

        # 分四次輸入數字，並設置輸入速度為指定的值
        pyautogui.write(full_number_str, interval=input_time)

        # 點擊送出按鈕
        pyautogui.click(submit_button_x, submit_button_y)

        # 休息指定的時間，以防止操作過快
        time.sleep(rest_time)

# 執行程式的函數
def execute_program():
    t = threading.Thread(target=start_program)
    t.start()

# 結束程式的函數
def stop_program():
    root.destroy()  # 結束程式

# 建立 Tkinter 窗口
root = tk.Tk()
root.title("自動輸入程式")

# 加入固定前4位數字和後2位數字的輸入框
prefix_label = tk.Label(root, text="請輸入前4位數字:")
prefix_label.pack()
prefix_entry = tk.Entry(root)
prefix_entry.pack()

suffix_label = tk.Label(root, text="請輸入最後2位數字:")
suffix_label.pack()
suffix_entry = tk.Entry(root)
suffix_entry.pack()

# 加入輸入框和送出按鈕座標的輸入框
input_box_x_label = tk.Label(root, text="請輸入輸入框 X 座標:")
input_box_x_label.pack()
input_box_x_entry = tk.Entry(root)
input_box_x_entry.pack()

input_box_y_label = tk.Label(root, text="請輸入輸入框 Y 座標:")
input_box_y_label.pack()
input_box_y_entry = tk.Entry(root)
input_box_y_entry.pack()

submit_button_x_label = tk.Label(root, text="請輸入送出按鈕 X 座標:")
submit_button_x_label.pack()
submit_button_x_entry = tk.Entry(root)
submit_button_x_entry.pack()

submit_button_y_label = tk.Label(root, text="請輸入送出按鈕 Y 座標:")
submit_button_y_label.pack()
submit_button_y_entry = tk.Entry(root)
submit_button_y_entry.pack()

# 加入輸入和休息時間的輸入框
input_time_label = tk.Label(root, text="請輸入輸入時間(秒):")
input_time_label.pack()
input_time_entry = tk.Entry(root)
input_time_entry.pack()

rest_time_label = tk.Label(root, text="請輸入休息時間(秒):")
rest_time_label.pack()
rest_time_entry = tk.Entry(root)
rest_time_entry.pack()

# 加入中間四位數的輸入框
middle_number_start_label = tk.Label(root, text="請輸入中間四位數起始值:")
middle_number_start_label.pack()
middle_number_start_entry = tk.Entry(root)
middle_number_start_entry.pack()

middle_number_end_label = tk.Label(root, text="請輸入中間四位數結束值:")
middle_number_end_label.pack()
middle_number_end_entry = tk.Entry(root)
middle_number_end_entry.pack()

# 加入開始執行和結束執行的按鈕
start_button = tk.Button(root, text="開始執行", command=execute_program)
start_button.pack()

stop_button = tk.Button(root, text="結束程式", command=stop_program)
stop_button.pack()

root.mainloop()
