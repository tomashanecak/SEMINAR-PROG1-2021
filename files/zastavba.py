## Zastavba
import os
import random
import tkinter as Tk

path = os.path.dirname(__file__)
filename = "zastavba.txt"

canvas = Tk.Canvas(width=500, height=500)
canvas.pack()

x = 10
y = 500

entry = Tk.Entry()

with open(filename, "r") as street:
    for building in street:
        dimensions = building.split(" ")

        if int(dimensions[0]) == 0:
            canvas.create_rectangle(x, y, x+int(dimensions[1].strip()), y-10, fill="green")
        canvas.create_rectangle(x, y, x+int(dimensions[1].strip()), y-int(dimensions[0].strip()), fill="black", outline="white")
        x += int(dimensions[1])


canvas.mainloop()