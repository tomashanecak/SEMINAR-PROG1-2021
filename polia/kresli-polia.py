import tkinter as tk
import random as r
from tkinter.constants import HORIZONTAL
from typing import Text

w = 1200
h = 700
root = tk.Tk()
canvas =tk.Canvas(width = w, height = h, background="white")
root.title("Kreslenie Pomocou Poľa")
canvas.pack()

color = "black"
colors = []
clr_prev_rect = canvas.create_rectangle(850,20, 1030, 80, fill=color)

def newPaper():
    canvas.delete("all")
    clr_prev_rect = canvas.create_rectangle(850,20, 1030, 80, fill=color)
    createBoard(10, generateColors(11))

new_btn = tk.Button(canvas, text="New Paper", command=newPaper)
new_btn.place(x=1050, y=40)

slider_red = tk.Scale(from_ = 0, to = 255, tickinterval= 50, orient=tk.HORIZONTAL, length=200)
slider_red.place(x=50, y=20)
slider_green = tk.Scale(from_ = 0, to = 255, tickinterval= 50, orient=tk.HORIZONTAL, length=200)
slider_green.place(x=300, y=20)
slider_blue = tk.Scale(from_ = 0, to = 255, tickinterval= 50, orient=tk.HORIZONTAL, length=200)
slider_blue.place(x=550, y=20)

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

def generateColors(dim):
    global colors
    colors =[]
    row = []

    for i in range(dim):
        if len(row) > 0: colors.append(row)
        row = []
        for j in range(dim):
            color = '#{:06x}'.format(r.randint(0, 256**3))
            row.append(color)

    return colors

def createBoard(dim, colors):
    for color in colors:
        print(color)

    y = 100
    size = 50
    for i in range(dim):
        x = 350
        y += 50
        for j in range(dim):
            canvas.create_rectangle(x, y, x+50, y+50, fill=colors[i][j])
            x+=50

def setColor(e):
    global colors
    print(e.x)
    print(e.y)

    if e.x > 350 and e.x < 850 and e.y > 150 and e.y < 650:
        j = (e.x - 350) // 50
        i = (e.y - 150) // 50
    else:
        print(" Wrong Coordinates! ")

    colors[i][j] = color
    canvas.delete("all")
    showColor()
    createBoard(10, colors)


newPaper()
canvas.bind("<Button-1>", setColor)
canvas.mainloop()