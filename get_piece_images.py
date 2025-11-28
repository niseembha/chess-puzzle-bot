import pyautogui
import time

def get_library_images():
    time.sleep(3)
    name = "black_rook_b1"
    img = pyautogui.screenshot(region=(309+50*3, 489+50*2, 46, 46))
    img.save(f"piece_images/library/{name}.png")

get_library_images()
