from tkinter import ttk
from tkinter import *
from ctypes import windll
import tkinter.messagebox
import sys, os, stop, timer, keyboard


## Set Default Variables and Functions
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


root = Tk()


root.mainloop()
