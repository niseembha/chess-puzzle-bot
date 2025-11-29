import pyautogui
import time

def get_library_images():
    time.sleep(3)
    name = "white_rook_w1"
    img = pyautogui.screenshot(region=(309+50*1, 489+50*1, 46, 46))
    img.save(f"piece_images/library/{name}.png")

get_library_images()
