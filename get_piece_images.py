import pyautogui
import time

# width and height of each square: 
# 46       46

# top left x, y:
#        309, 489
def get_real_time_images_of_board():
    time.sleep(3)
    x = 0
    y = 0
    i = 1
    j = 1
    for _ in range(8):
        for _ in range(8):
            name = ""
            match i:
                case 1:
                    name += "a"
                case 2:
                    name += "b"
                case 3:
                    name = "c"
                case 4:
                    name = "d"
                case 5:
                    name = "e"
                case 6:
                    name = "f"
                case 7:
                    name = "g"
                case 8:
                    name = "h"
            match j:
                case 1:
                    name += "8"
                case 2:
                    name += "7"
                case 3:
                    name += "6"
                case 4:
                    name += "5"
                case 5:
                    name += "4"
                case 6:
                    name += "3"
                case 7:
                    name += "2"
                case 8:
                    name += "1"        
            img = pyautogui.screenshot(region=(309+x, 489+y, 46, 46))
            img.save(f"piece_images/real_time/{name}.png")
            x += 50
            i += 1
        y += 50
        j += 1
        x = 0
        i = 1

def get_library_images():
    time.sleep(3)
    name = "white_king_w1"
    img = pyautogui.screenshot(region=(309+50*7, 489+50*7, 46, 46))
    img.save(f"piece_images/library/{name}.png")

get_library_images()
