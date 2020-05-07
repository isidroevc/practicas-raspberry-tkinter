#for python 3.x use 'tkinter' rather than 'Tkinter'
import tkinter as tk
import time

class App():
    def __init__(self, root, r, c):
        self.root = tk.Frame(root)
        self.root.grid(row=r, column=c)
        self.label = tk.Label(self.root, text="")
        self.label.pack()
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)


