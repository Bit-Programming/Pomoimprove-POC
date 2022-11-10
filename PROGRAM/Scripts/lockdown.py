import win32gui
import win32con

def startlockdown():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,100,200,200,win32con.SWP_NOMOVE|win32con.SWP_NOSIZE)