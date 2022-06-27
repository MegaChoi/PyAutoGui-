from mss import mss
import time
import keyboard
import win32api,win32con

start_x = 680
start_y = 600

# define a window on the screen where the game box is located 
bbox = (start_x,start_y,start_x + 310, start_y + 3)

# for coordinates for 4 columns of piano tiles
cords_x = [0,100,200,299]


def start():
    with mss() as sct:
        while keyboard.is_pressed('q') == False:
        #take a screen shot size of 300x1
            img = sct.grab(bbox)
            #check pixel RGB in the image where x values are ranged from 0 to 299 
            for cord in cords_x:
                # check if the R (RGB) value returned from .pixel is 0 
                if img.pixel(cord, 0)[0] == 0:
                    # if so set cursor 
                    win32api.SetCursorPos((start_x + cord, start_y))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    break

time.sleep(3)
start()
    
    
