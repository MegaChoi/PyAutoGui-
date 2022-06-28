import pyautogui
from mss import mss
import keyboard
import cv2 as cv 
import numpy as np
import time
# pyautogui.displayMousePosition()

bbox = (0,138,1903,1038)
#pyautogui no cooldown time
pyautogui.PAUSE = 0

AimDot = cv.imread('AimDot.JPG')
AimDot_grey = cv.cvtColor(AimDot, cv.COLOR_BGR2GRAY )
#OpenCV .shape (height,width,No. of Channels)
width = AimDot_grey.shape[0]
height = AimDot_grey.shape[1]

#game window dimensions 
x ,y ,w , h = 0,138,1903,1038
#wait
time.sleep(3)

def start ():
#main
    while keyboard.is_pressed('q') == False:
    #screen shot of the screen
        with mss() as sct:
            img = sct.grab(bbox)

        while True:
            img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            result = cv.matchTemplate(
                img_gray,
                AimDot_grey,
                cv.TM_CCOEFF_NORMED
            )

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

            #if the birghtest spot is >= 0.8
            if max_val >= 0.8:
                pyautogui.click(
                    max_loc[0] + x,
                    max_loc[1] + y,
                )

start()
    
