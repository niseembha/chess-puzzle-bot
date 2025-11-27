import pyautogui
import time

# width and height of each square: 
# 103       103

# top left x, y:
#        278, 141
def get_real_time_images_of_board(white_to_move):
    time.sleep(3)
    x = 0
    y = 0
    i = 1
    j = 1
    for _ in range(8):
        for _ in range(8):
            name = ""
            if white_to_move:
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
            else:
                match i:
                    case 1:
                        name += "h"
                    case 2:
                        name += "g"
                    case 3:
                        name = "f"
                    case 4:
                        name = "e"
                    case 5:
                        name = "d"
                    case 6:
                        name = "c"
                    case 7:
                        name = "b"
                    case 8:
                        name = "a"
                match j:
                    case 1:
                        name += "1"
                    case 2:
                        name += "2"
                    case 3:
                        name += "3"
                    case 4:
                        name += "4"
                    case 5:
                        name += "5"
                    case 6:
                        name += "6"
                    case 7:
                        name += "7"
                    case 8:
                        name += "8"                
            img = pyautogui.screenshot(region=(278+x, 141+y, 64, 64))
            img.save(f"piece_images/real_time/{name}.png")
            x += 103
            i += 1
        y += 103
        j += 1
        x = 0
        i = 1

def get_images_for_library():
    name = "black_bishop_highlightw"
    time.sleep(3)
    img = pyautogui.screenshot(region=(278+103*1, 141+103*1, 64, 64))
    img.save(f"piece_images/library/{name}.png")

# get_images_for_library()

from PIL import Image
import imagehash

img1 = Image.open("piece_images/library/black_bishop_white.png")
img2 = Image.open("piece_images/library/black_rook_white.png")

hash1 = imagehash.phash(img1)
hash2 = imagehash.phash(img2)

difference = abs(hash1 - hash2)

print("Hash difference:", difference)

if difference < 20:
    print("Images are similar")
else:
    print("Images are different")