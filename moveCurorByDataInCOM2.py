import serial
import time
import re  # 导入正则表达式模块
import pyautogui

pyautogui.FAILSAFE = False

start_x, start_y = 700, 700

# 配置串行端口
ser = serial.Serial('COM10', 9600, timeout=1)
time.sleep(2)  # 等待串行连接建立

print("Reading serial data. Press Ctrl+C to stop.")

def moveCurorFunc(x, y):
    global start_x, start_y

    x *= 50  # 假设归一化后的范围是0到100
    y *= 50

    # 将归一化后的值转换为屏幕上的坐标
    new_x = start_x + x
    new_y = start_y + y

    pyautogui.moveTo(new_x, new_y)
    start_x, start_y = new_x, new_y  # 更新起始坐标

    # time.sleep(0.1) # 休眠0.1秒


while True:
    # 读取串行端口的一行数据
    data = ser.readline()

    # 打印数据到控制台
    if data:
        print(f"Received: {data.decode().strip()}")

        # 使用正则表达式匹配浮点数
        match = re.search(r'Normalized x is ([0-9.]+) Normalized y is ([0-9.]+)', data.decode())
        if match:
            x_str, y_str = match.groups()
            x, y = float(x_str), float(y_str)
            x -= 0.36
            y -= 0.49
            print(f"Normalized x: {x}, Normalized y: {y}")
            
            moveCurorFunc(x, y)
