from tkinter import ttk
from tkinter import *
from ctypes import windll
import tkinter.messagebox
import sys, os, stop, timer

def timer():

    root = Tk()

    label = Label(root, text="test")
    label.place(x=35, y=15)


# Countdown Code for Timer
def countdown(count):
    print("Count: ")
    print(count)
    print("Minutes: ")
    print(minutes)
    # change text in label
    label["text"] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count - 1)
    elif count == 0:
        label["text"] = "DONE!"