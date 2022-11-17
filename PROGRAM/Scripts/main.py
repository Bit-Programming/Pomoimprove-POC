from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from ctypes import windll
import tkinter.messagebox
import lockdown, sys, os, stop, work, sv_ttk


## Enable HIDPI Support
windll.shcore.SetProcessDpiAwareness(1)


## Set Default Variables and Functions
# This will give us the path of the application, the path of Chrome, and the path to the logo.
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    os.chdir("..")
    application_path = os.getcwd()
chrome_path = application_path + "\Chrome\chrome.exe"
logo_path = application_path + "\Pomoimprove\PROGRAM\Images\Logo.png"

# Create popup about closing all windows
def closeWindowsPopup():
    message = tkinter.messagebox.askquestion("Ready to start?", "Are you ready to start working? This will close all open windows. You will not be able to go back until you are done with your assignment.")
    if message == 'yes':
        lockdown.secondlockdown()
        # CHANGE THIS ONCE WE FIGURE OUT THE ISSUE 
        work.work(5)


## Init Window
root = Tk()
# Set theme to dark mode
sv_ttk.set_theme("dark")
# Adjust window settings
root.title("Pomoimprove")
root.resizable(False, False)
root.overrideredirect(True)
root.state("zoomed")
# Define application button style
style = ttk.Style()
style.map(
    "C.TButton",
    foreground=[("pressed", "white"), ("active", "black")],
    background=[("pressed", "!disabled", "black"), ("active", "white")],
)


## Main Code
# Define "Quit" button hover actions
def on_enter_quit(e): # Change color when hovered over
    quitbutton['background'] = '#DB564D'
def on_leave_quit(e): # Revert color when no longer hovered over
    quitbutton['background'] = '#C71E12'
# Create "Quit" button
quitbutton = Button(
    root,
    bg="#C71E12",
    fg="#FFFFFF",
    borderwidth=0,
    text="Quit",
    font=("Segoe UI", 15),
    activeforeground="black",
    command=stop.stop)
# Bind hover actions
quitbutton.bind("<Enter>", on_enter_quit)
quitbutton.bind("<Leave>", on_leave_quit)
# Position "Quit" button to bottom left corner
quitbutton.place(relx=0, rely=1, anchor=SW)

# Add Pomoimprove text
Label(root, text="Pomoimprove", font=("Segoe UI", 30, "bold")).place(
    relx=0.5, rely=0.10, anchor=CENTER
)

# Add Pomoimprove Logo
logo_def = Image.open(logo_path)
logo = ImageTk.PhotoImage(logo_def)
logolabel = Label(image=logo)
logolabel.place(relx=0.5, rely=0.45, anchor=CENTER)

# Define "Start" button hover actions
def on_enter_start(e): # Change color when hovered over
    startbutton['background'] = '#7AFF6B'
def on_leave_start(e): # Revert color when no longer hovered over
    startbutton['background'] = '#3CC249'
# Create "Start" button
startbutton = Button(
    root,
    bg="#3CC249",
    fg="#FFFFFF",
    borderwidth=0,
    text="Start",
    font=("Segoe UI", 15),
    activeforeground="black",
    command=lambda: closeWindowsPopup())
# Bind hover actions
startbutton.bind("<Enter>", on_enter_start)
startbutton.bind("<Leave>", on_leave_start)
# Position "Quit" button to bottom left corner
startbutton.place(relx=0.5, rely=0.90, relheight=0.06, relwidth=0.10, anchor=CENTER)

# Close splash screen when app is loaded (pyinstaller)
if '_PYIBoot_SPLASH' in os.environ:
    # NOT an import error
    import pyi_splash
    pyi_splash.close

# Run lockdown code after running application
root.after(500, lockdown.firstlockdown)

root.mainloop()