from tkinter import ttk
from tkinter import *
from ctypes import windll
import tkinter.messagebox
import sys, os, stop, timer

def work(count):
    count = count - 1
    root = Tk()
    label = Label(root, text = count)
    label.place(x=35, y=15)

    print("Count: ")
    print(count)

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, work, count)
    elif count == 0:
        label["text"] = "DONE!"
work(5)
