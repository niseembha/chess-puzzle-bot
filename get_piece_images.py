import pyautogui
import time

def get_library_images():
    time.sleep(3)
    name = "white_queen_b1"
    img = pyautogui.screenshot(region=(309+50*7, 489+50*4, 46, 46))
    img.save(f"piece_images/library/{name}.png")

get_library_images()
