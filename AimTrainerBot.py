import pyautogui
from mss import mss
import keyboard
import cv2 as cv 
import time
# pyautogui.displayMousePosition()
time.sleep(3)
# bbox = (0,138,1903,1038)

start_x = 662
start_y = 341
#pyautogui no cooldown time
pyautogui.PAUSE = 0
def start(x,y):
    pyautogui.click(x,y)


while keyboard.is_pressed('q') == False:
    #take a screenshot of the game screen
    img = pyautogui.screenshot(region = (664,340,586,414))
    #got the 
    width, height = img.size

    for x in range(0,width,5):
        for y in range (0, height,5):
            b = img.getpixel((x,y))[2]
            if b == 195:
                # print(x + start_x, y + start_y)
                start(x + start_x, y + start_y)
                time.sleep(0.05)
                break
