from tkinter import *
from tkinter import ttk
root = Tk()

# Adjust window settings
root.configure(background="#AEAEAE")
root.title("Pomodoro App")
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
   Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)

# Code to add widgets will go here...
frm = ttk.Frame(root, padding=10)
frm.grid()


Label(root, text = "PomoImprove", font= ('Helvetica 25 bold')).place(relx=.5, rely=.5,anchor=CENTER)


#ttk.Label(frm, text="PomoImprove", font=('Mistral 18 bold')).grid(column=0, row=0, anchor=CENTER)

ttk.Button(frm, text="test popup", style="C.TButton", command=open_popup).place(relx=.5, rely=.5,anchor=CENTER)
ttk.Button(frm, text="Quit", style="C.TButton", command=root.destroy).place(relx=.5, rely=.5,anchor=N)


root.mainloop()
