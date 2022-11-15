from tkinter import ttk
from tkinter import *
import time, lockdown, sys, os


# Init Window
root = Tk()

# This will give us the path of the application and the path of Chrome.
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    os.chdir("..")
    application_path = os.getcwd()
chrome_path = application_path + "\Chrome\chrome.exe"

# Adjust window settings
root.configure(background="#AEAEAE")
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

# Functions

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


# Code to add widgets will go here...
frm = ttk.Frame(root, padding=10)
frm.grid()


# Specify Grid
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

Grid.rowconfigure(root, 1, weight=1)

# Create Buttons
pomodoros = Label(root, text="Pomodoros")
button_2 = Button(root, borderwidth=0, text="Quit", command=sys.exit)

# Set grid
# Stick to left side
pomodoros.grid(row=0, column=0, sticky="NSW")
button_2.grid(row=3, column=0, sticky="NSW")


# Main Pomoimprove Logo
Label(root, text="Pomoimprove", font=("Helvetica 25 bold"), bg="#AEAEAE").place(
    relx=0.5, rely=0.05, anchor=CENTER
)


# Timer length input boxes

hours = IntVar()
minutes = int()
minutes = 5

# Minutes = Entry(root, bg="#AEAEAE").place(relx=.53, rely=.35, relheight=.02, relwidth=.05, anchor=CENTER)

spinbox = Spinbox(
    root,
    bg="#AEAEAE",
    from_=0,
    to=60,
    increment=5,
    wrap=True,
    justify=CENTER,
    textvariable=minutes,
).place(relx=0.53, rely=0.25, relheight=0.02, relwidth=0.025, anchor=CENTER)


# call countdown first time
# root.after(0, countdown, 5)

# Needs to be before start/stop timer buttons
label = Label(root, text="test")
label.place(x=35, y=15)


# Make the start/stop timer buttons
Start = Button(
    root,
    bg="#3CC249",
    fg="#FFFFFF",
    borderwidth=0,
    text="Start",
    activeforeground="black",
    command=lambda: countdown((minutes)), # Send the value of the spinbox to timer function
).place(relx=0.50, rely=0.80, relheight=0.03, relwidth=0.05, anchor=CENTER)
Stop = Button(

    root,
    bg="#E33E3E",
    fg="#FFFFFF",
    borderwidth=0,
    text="Stop",
    activeforeground="black",
    command=lambda: countdown(0),
).place(relx=0.50, rely=0.85, relheight=0.03, relwidth=0.05, anchor=CENTER)


# finish implementing and assigning buttons and textbox to countdown function
countdown(3)

if '_PYIBoot_SPLASH' in os.environ:
    import pyi_splash
    pyi_splash.close()

root.after(500, lockdown.startlockdown)

root.mainloop()