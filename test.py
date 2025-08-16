import pyautogui
import numpy as np
import time

print(pyautogui.size())

# while True:
#     w = np.random.randint(0, 1512)
#     h = np.random.randint(0, 982)
#     pyautogui.moveTo(w, h, duration = 1)
#     time.sleep(5)

time.sleep(5)  # wait for 5 seconds before starting the movement
distance = 200
while distance > 0:
    pyautogui.doubleClick()  
    pyautogui.dragRel(distance, 0, duration=0.05, button='left')   # right
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0.05, button='left')   # down
    pyautogui.dragRel(-distance, 0, duration=0.05, button='left')  # left
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0.05, button='left')  # up