import pyautogui
import serial
import time

ser = serial.Serial('COM13', 9600, timeout=1) 
time.sleep(2) 

while True:
    data = ser.readline()
    number = int(data.decode().strip())
    number = abs(number)
    pyautogui.moveTo(number, number)

    print(number)

