import pyautogui
import time

time.sleep(3)
name = "black_to_move"
img = pyautogui.screenshot(region=(709, 504, 228, 33))
img.save(f"piece_images/library/{name}.png")