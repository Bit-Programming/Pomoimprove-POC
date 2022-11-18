import win32gui, win32con, sys, winreg, subprocess


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

        # Attempt to kill Explorer and Task Manager
        try:
            DETACHED_PROCESS = 0x00000008
            subprocess.call('taskkill /f /im explorer.exe', creationflags=DETACHED_PROCESS)
            subprocess.call('taskkill /f /im taskmgr.exe', creationflags=DETACHED_PROCESS)
        except:
            pass

        # Edit Registry to disable Task Manager
        reg_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(reg_key)


def secondlockdown():
    # Check if we are running in a compiled pyinstaller .exe, if not, don't run lockdown code
    if getattr(sys, 'frozen', False):
        # This code will close all windows, except for the main Pomoimprove window
        DETACHED_PROCESS = 0x00000008
        subprocess.call('powershell -EncodedCommand RwBlAHQALQBQAHIAbwBjAGUAcwBzACAAfAAgAFcAaABlAHIAZQAtAE8AYgBqAGUAYwB0ACAAewAoACQAXwAuAE0AYQBpAG4AVwBpAG4AZABvAHcAVABpAHQAbABlACAALQBuAGUAIAAiACIAKQAgAC0AYQBuAGQAIAAoACQAXwAuAE0AYQBpAG4AVwBpAG4AZABvAHcAVABpAHQAbABlACAALQBuAGUAIAAiAFAAbwBtAG8AaQBtAHAAcgBvAHYAZQAiACkAfQAgAHwAIABzAHQAbwBwAC0AcAByAG8AYwBlAHMAcwA=', creationflags=DETACHED_PROCESS)
