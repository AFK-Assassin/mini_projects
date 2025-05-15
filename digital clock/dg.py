import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime(" %H:%M:%S %p \n %d/%m/%y")
    label.config(text=string)
    label.after(1000, time)

try:
    clock_font = ("DS-Digital", 100, "bold")
except:
    clock_font = ("Arial", 100, "bold")

label = tk.Label(root, font=clock_font, background="black", foreground="blue")
label.pack(anchor="center")

time()
root.mainloop()
