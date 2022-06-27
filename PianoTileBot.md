# PyAutoGui-
Libaries required :

from mss import mss
import time
import keyboard
import win32api,win32con


mss is the alternative from pyautogui since it's faster
mss is used to take screenshots 

win32 is used to move cursor and perform click function

###

start by defining the location x and y of piano tile

array cords_x of the center of 4 columns of piano tile

1) mss takes a screen shot of predefined location of piano tile on the screen
2) the for loop check RGB values of all center of the 4 columns of piano tile, if the R value returned 0 (black) then win32 (click) is executed 
