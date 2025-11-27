import pyautogui

img = pyautogui.screenshot(region=(278, 141, 825, 825))
img.save("region.png")