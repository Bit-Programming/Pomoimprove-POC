from tkinter import ttk
from tkinter import *
from ctypes import windll
import tkinter.messagebox
import lockdown, sys, os, stop, timer, sv_ttk

# Enable HIDPI Support
windll.shcore.SetProcessDpiAwareness(1)


## Set Default Variables and Functions
# This will give us the path of the application and the path of Chrome.
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    os.chdir("..")
    application_path = os.getcwd()
chrome_path = application_path + "\Chrome\chrome.exe"

# Create popup about closing all windows
def closeWindowsPopup():
    message = tkinter.messagebox.askquestion("Ready to start?", "Are you ready to start working? This will close all open windows. You will not be able to go back until you are done with your assignment.")

    if message == 'yes':
        lockdown.secondlockdown()
        timer.countdown(5)


## Init Window
root = Tk()
sv_ttk.set_theme("dark")

# Adjust window settings
root.title("Pomoimprove")
root.resizable(False, False)
root.overrideredirect(True)

# Set window to be maximized by default
root.state("zoomed")

# Define document styles
style = ttk.Style()
style.map(
    "C.TButton",
    foreground=[("pressed", "white"), ("active", "black")],
    background=[("pressed", "!disabled", "black"), ("active", "white")],
)

# Specify Grid
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)


## Main Code
# Create Buttons
def on_enter(e): # Change color when hovered over
    button_2['background'] = '#61cbfc'

def on_leave(e): # Revert color when no longer hovered over
    button_2['background'] = '#1c1c1c'

button_2 = Button(root, borderwidth=1, text="Quit", height=3, width=10, command=stop.stop)
button_2.bind("<Enter>", on_enter)
button_2.bind("<Leave>", on_leave)

# Set grid
# Stick to left side
button_2.grid(row=3, column=0, sticky="NSW")

# Main Pomoimprove Logo
Label(root, text="Pomoimprove", font=("Segoe UI", 30, "bold")).place(
    relx=0.5, rely=0.05, anchor=CENTER
)

# Make the "Start" Timer button
Start = Button(
    root,
    bg="#3CC249",
    fg="#FFFFFF",
    borderwidth=0,
    text="Start",
    font=("Segoe UI", 15),
    activeforeground="black",
    command=lambda: closeWindowsPopup()
).place(relx=0.5, rely=0.80, relheight=0.06, relwidth=0.10, anchor=CENTER)

# Close splash screen when app is loaded
if '_PYIBoot_SPLASH' in os.environ:
    # NOT an import error
    import pyi_splash
    pyi_splash.close

# Run lockdown code after running application
root.after(500, lockdown.firstlockdown)

root.mainloop()