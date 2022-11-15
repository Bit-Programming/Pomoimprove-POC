import win32gui, win32con, win32ui, os, sys, winreg

# Set Registry Values for disabling Task Manager
registry_path: str = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
registry_name: str = "DisableTaskMgr"
value: int = 1

def firstlockdown():
    # Check if we are running in a compiled pyinstaller .exe, if not, don't run lockdown code
    if getattr(sys, 'frozen', False):
        # Find the "Pomoimprove" window, set as "hwnd"
        hwnd = win32gui.FindWindowEx(None, None, None, "Pomoimprove")
        # Put "Pomoimprove" window on top
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOPMOST,
            0,
            100,
            200,
            200,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE,
        )

        # Kill Explorer, if Explorer is running
        if win32ui.FindWindow(None, "Explorer"):
            os.system("taskkill /f /im explorer.exe")

        # Edit Registry to disable Task Manager
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(reg_key)
