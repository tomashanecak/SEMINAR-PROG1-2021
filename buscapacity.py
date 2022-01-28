import os
import tkinter as Tk

path = os.path.dirname(__file__)

w = 500; h = 500
canvas = Tk.Canvas(width=w, height=h)
canvas.pack()

stops = []
stop_status = []
max_capacity = 0

def load_bus():
    global stop_status
    global stops
    global max_capacity

    with open(os.path.join(path, "buscapacity.txt"), "r") as busfile:
        max_capacity = int(busfile.readline())

        for i, stop in enumerate(busfile):
            stop = stop.split(" ")
            get_on = int(stop.pop(0))
            get_off = int(stop.pop(0))
            stop = "".join(stop)

            if i == 0:
                stop_status.append(get_on)
            else:
                stop_status.append((stop_status[-1] + get_on) - get_off)

            stops.append(stop)

def draw_stops():
    x = 100
    y = 50
    spacing = 40

    for i, stop in enumerate(stops):
        canvas.create_text(x, y, text=stop, anchor="w")
        canvas.create_rectangle(x+150, y-(spacing/2), x+300, y+(spacing/3))
        
        percent = (stop_status[i] / max_capacity) * 100
        pixels = percent*1.5

        if percent >= 100:
            color = "red"
        else:
            color = "green"

        canvas.create_rectangle(x+150, y-(spacing/2), x+150+pixels, y+(spacing/3), fill=color)
        y += spacing

load_bus()
draw_stops()

canvas.mainloop()