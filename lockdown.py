import win32gui
import win32con
import os

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,200,200,0)

#test
test = os.popen('tasklist').readlines()

print(test)