from tkinter import ttk
from tkinter import *
from ctypes import windll
import tkinter.messagebox
import sys, os, stop, timer




# Countdown Code for Timer
def work(count):    
    root = Tk()
    label = Label(root)
    label.place(x=35, y=15)
    
    print("Count: ")
    print(count)
    # change text in label
    label["text"] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, work, count - 1)
    elif count == 0:
        label["text"] = "DONE!"
        