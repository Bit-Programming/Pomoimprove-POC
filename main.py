from tkinter import *
from tkinter import ttk
root = Tk()

# Adjust window settings
root.configure(background="#AEAEAE")
root.title("Pomodoro App")
root.geometry("500x500")
root.state("zoomed")

# Define document styles
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

# Code to add widgets will go here...
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="PomoImprove").grid(column=0, row=0)
ttk.Button(frm, text="Quit", style="C.TButton", command=root.destroy).grid(column=1, row=0)

root.mainloop()
