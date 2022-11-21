from tkinter import ttk
from tkinter import *
from ctypes import windll
import tkinter.messagebox
import config, sv_ttk, keyboard, subprocess


## Enable HIDPI Support
windll.shcore.SetProcessDpiAwareness(1)


## Set Default Variables and Functions
# Prompt for Google account signin
def googleAccountPopup():
    message = tkinter.messagebox.showinfo("Google Account", "To proceed with this application, you must sign into your Google Account. Your Google Account will be signed out of once the experiment is concluded. After you sign in, please close out of the window.")
    # This code below will open the Chrome window, no matter what they answer to the question
    if message != '':
        # Start Chrome for person to signin
        DETACHED_PROCESS = 0x00000008
        subprocess.call(config.chrome_path + " --new-window --app=https://accounts.google.com", creationflags=DETACHED_PROCESS)
# Prompt for Spotify account signin
def spotifyAccountPopup():
    message = tkinter.messagebox.askquestion("Spotify Account", "If you want to, you can sign into your Spotify account and play music in the background while you are working. This is known to further increase productivity. Once signed in, close out of the window.")
    if message == 'yes':
        # Set a variable so we know that they have a Spotify account
        spotifyaccount = 1
        DETACHED_PROCESS = 0x00000008
        subprocess.call(config.chrome_path + " --new-window --app=https://accounts.spotify.com/en/login", creationflags=DETACHED_PROCESS)
    else:
        spotifyaccount = 0

# Make function to quit out of the timer and Chrome
def quit():
    # Attempt to kill Chrome
    try:
        DETACHED_PROCESS = 0x00000008
        subprocess.call('taskkill /F /IM exename.exe', creationflags=DETACHED_PROCESS)
    except:
        pass
    # Destroy the root window(s)
    root.destroy()
# Setup keyboard shortcut to quit the "work" part of the program
keyboard.add_hotkey('ctrl + alt + shift + b + i + t', quit)

# Define the timer code
def timer():
    # Set "time" as a global variable
    global time
    if time == 0:
        timerlabel.config(text = "DONE")
        # ADD VARIABLE FUNCTION
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
sv_ttk.set_theme("dark")

# Set window on top
root.call('wm', 'attributes', '.', '-topmost', '1')

# Set window size
root.geometry("100x100")

timerlabel = Label(root, text="", font=("Segoe UI", 10, "bold"))
timerlabel.place(relx=0.5, rely=0.5, anchor=CENTER)
time = 60
root.after(1000, timer)

root.mainloop()
