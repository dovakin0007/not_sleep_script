from ctypes import Structure, windll, c_uint, sizeof, byref
import time
import numpy as np
from math import cos,sin
import pyautogui
# http://stackoverflow.com/questions/911856/detecting-idle-time-in-python
class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]
def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime

    return millis / 1000.0

while True:
    time_idle = (int(get_idle_duration()))
    print(time_idle)
    time.sleep(1)
    if time_idle >= 180:
        pyautogui.press('space')
        time.sleep(10)
        time.sleep('left')
        time.sleep(1)
        pyautogui.press('space')

        

