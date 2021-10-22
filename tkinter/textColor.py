import tkinter as tk
import random as r

h = 500
w = h
canvas = tk.Canvas(width=w, height=h, background="white")
canvas.pack()

text = str(input("Zadaj text: "))

def checkColor(forbidden = "red"):
    color = generateColor()
    if color == forbidden:
        generateColor()
    else:
        return color

def generateColor():
    colors = "red", "green", "blue", "yellow", "orange", "purple"
    return r.choice(colors)

def drawText(color):
    canvas.create_text(r.randint(0,w), r.randint(0,h), text=text, fill=color)
    canvas.after(1000)
    canvas.update()
    drawText(color)

def click(e):
    canvas.delete("all")
    drawText(checkColor())

canvas.bind("<ButtonPress-1>", click)
canvas.mainloop()




    