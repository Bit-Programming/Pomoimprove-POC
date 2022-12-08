from tkinter import ttk
from tkinter import *
from ctypes import windll
import tkinter.messagebox
import time as sleep
import config, keyboard, subprocess, os, shutil, threading, window


## Enable HIDPI Support
windll.shcore.SetProcessDpiAwareness(1)


## Set Default Variables and Functions
# Prompt for Google account signin
def googleAccountPopup():
    tkinter.messagebox.showinfo("Google Account", "To proceed with this application, you must sign into your Google Account. Your Google Account will be signed out of once the experiment is concluded. After you see the blocked screen, close out of the window.")
    # Start Chrome for person to signin
    DETACHED_PROCESS = 0x00000008
    subprocess.call(config.chrome_path + " --new-window --app=https://accounts.google.com", creationflags=DETACHED_PROCESS)
# Prompt for Spotify account signin
def spotifyAccountPopup():
    message = tkinter.messagebox.askquestion("Spotify Account", "If you want to, you can sign into your Spotify account and play music in the background while you are working. This is known to further increase productivity. Once you sign in, close out of the window.")
    global spotifyaccount
    if message == 'yes':
        # Set a variable so we know that they have a Spotify account
        spotifyaccount = True
        # Start Chrome for person to signin
        DETACHED_PROCESS = 0x00000008
        subprocess.call(config.chrome_path + " --new-window --app=https://accounts.spotify.com/en/login", creationflags=DETACHED_PROCESS)
    else:
        # Set a variable so we know that they don't have a Spotify account
        spotifyaccount = False

# Prevent window from being able to be closed
def preventClose():
    pass

# Setup function to open Spotify and allow them to pick music for 1 minute
def spotifyMusic():
    # Set a variable to a function to run once the timer is done
    global run
    run = firstWorkPeriod
    # Set the time for the timer
    global time
    time = 60
    # Try to close the YouTube window
    try:
        window.find_window_wildcard(".*YouTube")
        window.close(window.hwnd)
    except:
        pass
    # Run the timer
    root.after(1000, timer)
    # Start the Chrome Spotify window
    subprocess.Popen([config.chrome_path, "--new-window", "--app=https://open.spotify.com"], creationflags=subprocess.DETACHED_PROCESS)

# Setup the long break period
def longBreakPeriod():
    # Set a variable to a function to run once the timer is done, to Spotify if spotifyaccount = true, otherwise, to the first work period
    global run
    if spotifyaccount == True:
        run = spotifyMusic
    else:
        run = firstWorkPeriod
    # Set the time for the timer
    global time
    time = 600
    # Run the timer
    root.after(1000, timer)
    # Start the Chrome YouTube window
    subprocess.Popen([config.chrome_path, "--new-window", "--window-position=500,0", "--app=https://youtube.com"], creationflags=subprocess.DETACHED_PROCESS)
# Setup the short break period
def shortBreakPeriod():
    # Set a variable to a function to run once the timer is done
    global run
    run = workPeriod
    # Set the time for the timer
    global time
    time = 300
    # Try to hide "Google Docs" and activate "Spotify"
    try:
        window.find_window_wildcard(".*Google Docs")
        window.minimize(window.hwnd)
        window.find_window_wildcard("Spotify -*")
        window.activate(window.hwnd)
    except:
        pass
    # Run the timer
    root.after(1000, timer)
    # Start the Chrome YouTube window
    subprocess.Popen([config.chrome_path, "--new-window", "--window-position=500,0", "--app=https://youtube.com"], creationflags=subprocess.DETACHED_PROCESS)
# Setup the first work period
def firstWorkPeriod():
    # Set a variable to a function to run once the timer is done
    global run
    run = shortBreakPeriod
    # Set the time for the timer
    global time
    time = 600
    # Try to close the YouTube window and minimize the Spotify window
    try:
        window.find_window_wildcard(".*YouTube")
        window.close(window.hwnd)
        window.find_window_wildcard("Spotify -*")
        window.minimize(window.hwnd)
    except:
        pass
    # Run the timer
    root.after(1000, timer)
    # Start the Chrome Google Docs window
    subprocess.Popen([config.chrome_path, "--new-window", "--start-fullscreen", "--app=https://docs.google.com/document/u/0/create?usp=dot_new"], creationflags=subprocess.DETACHED_PROCESS)
# Setup the other work periods
def workPeriod():
    # Set a variable to a function to run once the timer is done
    global run
    run = shortBreakPeriod
    # Set the time for the timer
    global time
    time = 600
    # Try to close the YouTube window and minimize the Spotify window
    try:
        window.find_window_wildcard(".*YouTube")
        window.close(window.hwnd)
        window.find_window_wildcard("Spotify -*")
        window.minimize(window.hwnd)
    except:
        pass
    # Run the timer
    root.after(1000, timer)
    # Activate the Chrome Google Docs window
    window.find_window_wildcard(".*Google Docs")
    window.activate(window.hwnd)

# Make function to quit out of the timer and Chrome
def quit():
    # Attempt to kill Chrome
    try:
        DETACHED_PROCESS = 0x00000008
        subprocess.call('taskkill /F /IM chrome.exe', creationflags=DETACHED_PROCESS)
    except:
        pass
    # Find "AppData" location
    appdata = os.getenv("LOCALAPPDATA")
    sleep.sleep(1)
    # Try to delete the Chromium data directory
    try:
        shutil.rmtree(appdata + "\\Chromium\\")
    except:
        pass
    # Try to destroy the root window(s)
    try:
        root.destroy()
    except:
        pass
# Setup keyboard shortcut to quit the "work" part of the program
keyboard.add_hotkey('ctrl + alt + shift + b + i + t', quit)

# Define the timer code
def timer():
    # Set "time" as a global variable
    global time
    if time == 0:
        run()
    else:
        time = time - 1 # Take away 1 from the time
        global minute
        minute = time // 60
        seconds = time - minute * 60
        if seconds < 10:
            timerlabel.config(text = str(minute) + ":" + "0" + str(seconds)) # Change text on timer, and add 0 as needed
        else:
            timerlabel.config(text = str(minute) + ":" + str(seconds)) # Change text on timer
        root.after(1000, timer) # Wait one second, then repeat
        root.update() # Update window

## Main Code
# Open prompt asking to sign into your Google Account
googleAccountPopup()
# Open prompt asking if you want to sign into your Spotify account
spotifyAccountPopup()

# Init Window
root = Tk()
root.title("Pomoimprove")
root.resizable(False, False)
root.overrideredirect(True)
root.state("normal")
root.configure(bg="#1c1c1c")
root.protocol("WM_DELETE_WINDOW", preventClose)

# Set window on top
root.call('wm', 'attributes', '.', '-topmost', '1')

# Set window size
root.geometry("250x180")

# Setup the label for the timer
timerlabel = Label(root, text="", font=("Segoe UI", 30, "bold"), background="#1c1c1c", foreground="#FFFFFF")
timerlabel.place(relx=0.5, rely=0.5, anchor=CENTER)

# Start first break period, which will call other functions once it is done.
longBreakPeriod()


root.mainloop()
