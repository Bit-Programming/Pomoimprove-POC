from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import time

root = Tk()

# Adjust window settings
root.configure(background="#F0F0F0")
root.title("Pomoimprove")
root.resizable(False,False)
root.overrideredirect(True)
# Set window to be maximized by default
root.state("zoomed")

# Define document styles
style=ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

# Functions
def open_popup():
   top=Toplevel(root)
   top.geometry("750x250")
   top.title("Child Window")
   Label(top, text="Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)

# Code to add widgets will go here...
frm = ttk.Frame(root, padding=10)
frm.grid()



# Specify Grid
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)
 
Grid.rowconfigure(root,1,weight=1)
 
# Create Buttons
pomodoros = Label(root,text="Pomdoros")
button_2 = Button(root,text="Settings")
 
# Set grid
# Stick to left side
pomodoros.grid(row=0,column=0,sticky="NSW")
button_2.grid(row=3,column=0,sticky="NSW")






Label(root, text="Pomoimprove", font=('Helvetica 25 bold')).place(relx=.5, rely=.5,anchor=CENTER)

ttk.Button(frm, text="test popup", style="C.TButton", command=open_popup).grid(column=1, row=2)
ttk.Button(frm, text="Quit", style="C.TButton", command=root.destroy).grid(column=1, row=0)







def countdown(count):
    # change text in label        
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    elif count == 0:
        label['text'] = "DONE!"



label = Label(root)
label.place(x=35, y=15)

# call countdown first time    
countdown(5)
# root.after(0, countdown, 5)

root.mainloop()
