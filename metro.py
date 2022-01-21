import tkinter
import os

from numpy import angle

width, height = 600, 500
canvas = tkinter.Canvas(width = width, height = height)
canvas.pack()

filepath = os.path.dirname(__file__)

def load_path(filename):
    with open(os.path.join(filepath, str(filename)), "r") as path:
        color = path.readline().strip()
        length = width - 100
        stations = []
        x = 50
        y = height/2
        canvas.create_line(x, y, width-x, y, fill=color)

        for row in path:
            stations.append(row)

        distance = length / (len(stations)-1)
        for station in stations:
            canvas.create_oval(x, y-10, x+15, y+8, fill=color)
            canvas.create_text(x+10, y-25, angle=45, anchor="sw", text=station)
            x += distance

load_path("trasa_1_metro.txt")

canvas.mainloop()