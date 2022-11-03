from tkinter import *
from tkinter import ttk
root = Tk()

# Adjust window settings
root.configure(background="#AEAEAE")
root.title("Pomodoro App")
# For setting the window size on unmaxize
root.geometry("500x500")
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
   Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)

# Code to add widgets will go here...
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="PomoImprove", font=('Mistral 18 bold')).grid(column=0, row=0)

ttk.Button(frm, text="test popup", style="C.TButton", command=open_popup).grid(column=1, row=2)
ttk.Button(frm, text="Quit", style="C.TButton", command=root.destroy).grid(column=1, row=0)


root.mainloop()
