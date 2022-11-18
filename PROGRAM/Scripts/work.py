from tkinter import ttk
from tkinter import *
from ctypes import windll
import tkinter.messagebox
import config, os, sv_ttk, keyboard


## Enable HIDPI Support
windll.shcore.SetProcessDpiAwareness(1)


## Set Default Variables and Functions
# Prompt for Google account signin
def googleAccountPopup():
    message = tkinter.messagebox.showinfo("Google Account", "To proceed with this application, you must sign into your Google Account. Your Google Account will be signed out of once the experiment is concluded. After you sign in, please close out of the window.")
    if message == 'ok':
        os.system(config.chrome_path + " --new-window --app=https://accounts.google.com")

# Make function to quit out of the timer and Chrome
def quit():
    # Attempt to kill Chrome
    try:
        os.system("taskkill /f /im chrome.exe")
    except:
        pass
    # Destroy the root window(s)
    root.destroy()
# Setup keyboard shortcut to quit the "work" part of the program
keyboard.add_hotkey('ctrl + alt + shift + b + i + t', quit)


## Main Code
# Open prompt asking to sign into your Google Account
googleAccountPopup()

# Init Window
root = Tk()
root.title("Pomoimprove")
root.resizable(False, False)
root.overrideredirect(True)
root.state("normal")


root.mainloop()
