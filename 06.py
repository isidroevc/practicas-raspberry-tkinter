#for python 3.x use 'tkinter' rather than 'Tkinter'
import tkinter as tk
import time

def update_clock():
    now = time.strftime("%d/%m/%y %H:%M:%S")
    label.configure(text=now)
    root.after(1000, update_clock)
    
root = tk.Tk()
label = tk.Label(text="")
label.pack()
update_clock()
root.mainloop()
