import win32gui, win32con, re


## Functions for finding the hwnd of a window by a wildcard in the window title
def _window_enum_callback(hwndvalue, wildcard):
    # See if any windows have the specified wildcard in the window title
    if re.match(wildcard, str(win32gui.GetWindowText(hwndvalue))) is not None:
        # Set hwnd as global
        global hwnd
        # Set hwnd as equal to hwndvalue
        hwnd = hwndvalue

def find_window_wildcard(wildcard):
    # Find a window whose title matches the wildcard regex
    global hwnd
    hwnd = None
    win32gui.EnumWindows(_window_enum_callback, wildcard)


## Minimize/Activate/Close functions
def minimize(hwndvalue):
    win32gui.ShowWindow(hwndvalue, win32con.SW_MINIMIZE)

def activate(hwndvalue):
    win32gui.ShowWindow(hwndvalue, win32con.SW_SHOWNOACTIVATE)

def close(hwndvalue):
    win32gui.PostMessage(hwndvalue, win32con.WM_CLOSE)
