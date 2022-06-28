import pyautogui
import keyboard
import time 
time.sleep(3)
pyautogui.PAUSE = 0
pyautogui.displayMousePosition()
# while keyboard.is_pressed('q') == False:
#     AimDot = pyautogui.locateOnScreen('AimDot.JPG', confidence = 0.8)
#     Center = pyautogui.center(AimDot)
#     x,y = Center 
#     pyautogui.click(x,y)