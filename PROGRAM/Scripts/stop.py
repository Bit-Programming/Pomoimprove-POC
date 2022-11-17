import os
import sys
import winreg


# Set Registry values for enabling Task Manager
registry_path: str = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
registry_name: str = "DisableTaskMgr"
value: int = 0


def stop():
    # Check if we are running in a compiled pyinstaller .exe, if not, don't run extra code
    if getattr(sys, 'frozen', False):
        # Run Explorer
        os.startfile("C:\Windows\explorer.exe")

        # Edit Registry to enable Task Manager
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(reg_key)
    # Exit out of the program
    sys.exit()
