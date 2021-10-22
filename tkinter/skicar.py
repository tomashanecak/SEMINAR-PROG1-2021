import tkinter as tk
import random as r
from tkinter.constants import HORIZONTAL
from typing import Text

w = 1200
h = 700
canvas =tk.Canvas(width = w, height = h, background="white")
canvas.pack()

color = "#ffffff"
shape = ""
line_start = 0
old_line_x = 0
old_line_y = 0

canvas.create_line(0, 120, w, 120)
canvas.create_line(0, h-120, w, h-120)
slider_red = tk.Scale(from_ = 0, to = 255, tickinterval= 50, orient=tk.HORIZONTAL, length=200)
slider_red.place(x=50, y=20)
slider_green = tk.Scale(from_ = 0, to = 255, tickinterval= 50, orient=tk.HORIZONTAL, length=200)
slider_green.place(x=300, y=20)
slider_blue = tk.Scale(from_ = 0, to = 255, tickinterval= 50, orient=tk.HORIZONTAL, length=200)
slider_blue.place(x=550, y=20)

slider_rect = tk.Scale(from_ = 0, to = 100, tickinterval= 20, orient=tk.HORIZONTAL, length=200)
slider_rect.place(x=50, y=h-80)
slider_oval = tk.Scale(from_ = 0, to = 100, tickinterval= 20, orient=tk.HORIZONTAL, length=200)
slider_oval.place(x=280, y=h-80)
slider_line = tk.Scale(from_ = 0, to = 100, tickinterval= 20, orient=tk.HORIZONTAL, length=200)
slider_line.place(x=660, y=h-80)
slider_erase = tk.Scale(from_ = 0, to = 100, tickinterval= 20, orient=tk.HORIZONTAL, length=200)
slider_erase.place(x=940, y=h-80)

clr_prev_rect = canvas.create_rectangle(850,20, 1030, 80, fill=color)
def showColor():
    global slider_red, slider_green, slider_blue, clr_prev_rect, color
    canvas.delete(clr_prev_rect)
    r = slider_red.get()
    g = slider_green.get()
    b = slider_blue.get()
    color = f"#{r:02x}{g:02x}{b:02x}"
    clr_prev_rect = canvas.create_rectangle(850,20, 1030, 80, fill=color)

clr_prev_btn = tk.Button(canvas, text="Set Color", command=showColor)
clr_prev_btn.place(x=895, y=85)

def setRect():
    global shape
    shape = "Rectangle"

def setOval():
    global shape
    shape = "Oval"

def setNewLine():
    global shape, line_start
    shape = "New Line"
    line_start=0

def setErase():
    global shape
    shape = "Erase"

def draw(e):
    if shape == "Rectangle":
        size = slider_rect.get()
        canvas.create_rectangle(e.x, e.y, e.x+size, e.y+size, fill=color)

    if shape == "Oval":
        size = slider_oval.get()
        canvas.create_oval(e.x, e.y, e.x+size, e.y+size, fill=color)

    if shape == "Erase":
        size = slider_erase.get()
        canvas.create_oval(e.x, e.y, e.x+size, e.y+size, fill="white", outline="white")

    if shape == "New Line":
        global old_line_x, old_line_y, line_start

        if line_start == 0:
            old_line_x = e.x
            old_line_y = e.y
            line_start = 1

        elif line_start == 1:
            size = slider_line.get()
            canvas.create_line(old_line_x, old_line_y, e.x, e.y, width=size, fill=color)
            old_line_x = e.x
            old_line_y = e.y

draw_btn = tk.Button(canvas, text="Rectangle", command=setRect)
draw_btn.place(x=100, y=h-115)
draw_btn = tk.Button(canvas, text="Oval", command=setOval)
draw_btn.place(x=350, y=h-115)
draw_btn = tk.Button(canvas, text="New Line", command=setNewLine)
draw_btn.place(x=710, y=h-115)
draw_btn = tk.Button(canvas, text="Erase", command=setErase)
draw_btn.place(x=1000, y=h-115)

canvas.bind("<Button-1>", draw)
canvas.bind("<B1-Motion>", draw)
canvas.mainloop()