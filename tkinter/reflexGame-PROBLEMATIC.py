import tkinter as tk
import random as r
from tkinter.constants import X 

w = 500
h = 600
canvas = tk.Canvas(width=w, height=h, background="white")
canvas.pack()

circle = canvas.create_oval(0, 0, 10, 10)
colors = "violet", "green", "blue", "yellow", "orange", "pink", "grey" 
size = 50

x = 0
y = 0

def drawRandomCircle():
    canvas.after(2000)
    canvas.update()

    global circle
    canvas.delete(circle)

    global x
    global y
    x = r.randint(0, w-50)
    y = r.randint(0, h-50)
    circle = canvas.create_rectangle(x, y, x+size, y+size, fill=r.choice(colors))

def onClick(event): 

    canvas.delete(all)
    canvas.create_text(100,100,text=str(x))
    canvas.create_text(100,150,text=str(y))
    canvas.create_text(100,200,text=str(event.x))
    canvas.create_text(100,250,text=str(event.y))


    # if event.x > x and event.x < (x + size):

    



while True:
    drawRandomCircle()
    canvas.bind("<Button-1>", onClick)
    



canvas.mainloop()