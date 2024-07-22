import pyautogui
import time

# # Wait for 2 seconds to give you time to switch to another window if needed
# time.sleep(2)

# # Move the cursor to position (100, 100)
# pyautogui.moveTo(100, 100)

# # Wait for 1 second
# time.sleep(1)

# # Move the cursor to position (500, 500)
# pyautogui.moveTo(500, 500)
# time.sleep(1)

pyautogui.moveTo(100, 100)
time.sleep(1)

pyautogui.moveTo(200, 200)
time.sleep(1)

pyautogui.moveTo(300, 300)
time.sleep(1)

pyautogui.moveTo(400, 400)
time.sleep(1)

pyautogui.moveTo(500, 500)
time.sleep(1)

pyautogui.moveTo(600, 600)
time.sleep(1)

pyautogui.moveTo(700, 700)
time.sleep(1)

# Initial position of the cursor
start_x, start_y = 700, 700

# Move the cursor to the initial position
pyautogui.moveTo(start_x, start_y)

# Move the cursor continuously
for i in range(100):
    pyautogui.moveTo(start_x + i, start_y + i)
    time.sleep(0.01)  # Sleep for 10 milliseconds between movements