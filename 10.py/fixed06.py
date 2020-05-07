#for python 3.x use 'tkinter' rather than 'Tkinter'
import tkinter as tk
import time
def getExample06(root, r, c):
	def update_clock():
		now = time.strftime("%d/%m/%y %H:%M:%S")
		label.configure(text=now)
		root.after(1000, update_clock)
	frame = tk.Frame(root)
	frame.grid(row=r, column=c)
	label = tk.Label(frame, text="")
	label.pack()
	update_clock()

