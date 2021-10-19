import tkinter as tk
import random as r

w = 800
h = w
canvas = tk.Canvas(width = w, height = h, background="white")
canvas.pack()

xglob1 = 10
xglob2 = 10

def drawCar(x,y, color):
    canvas.create_polygon(x, y, x+60, y, x+70, y+20, x+100, y+20, x+100, y+50, x, y+50, x, y, fill=color)
    canvas.create_oval(x+10, y+35, x+35, y+60, fill="black")
    canvas.create_oval(x+55, y+35, x+80, y+60, fill="black")

def drawGame(start):
    canvas.create_line(start, 0, start, h)
    canvas.create_line(w-start, 0, w-start, h)

def race():
    global xglob1
    global xglob2
    xglob1 += r.randint(1,15)
    xglob2 += r.randint(1,15)
    
    canvas.delete("all")
    drawGame(115)
    drawCar(xglob1, 100, "blue")
    drawCar(xglob2, 300, "red")

    canvas.after(100)
    canvas.update()
    checkWinner(xglob1, xglob2)

def checkWinner(xcar1, xcar2):
    if (xcar1+100) >= (w-115):
        canvas.create_text(w/2, h/2, text="Blue is the winner!")
    elif (xcar2+100) >= (w-115):
        canvas.create_text(w/2, h/2, text="Red is the winner!")
    else:
        race()

startBtn = tk.Button(canvas, text="Start the race!", command=race).place(x=(w/2)-50, y=h-200)

drawGame(115)
drawCar(xglob1, 100, "blue")
drawCar(xglob2, 300, "red")

canvas.mainloop()