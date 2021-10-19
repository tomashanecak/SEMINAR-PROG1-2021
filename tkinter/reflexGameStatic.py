import tkinter as tk
import random as r
from tkinter.constants import X 
import time

w = 500
h = 600
canvas = tk.Canvas(width=w, height=h, background="white")
canvas.pack()

circle = canvas.create_oval(0, 0, 10, 10)
colors = "violet", "green", "blue", "yellow", "orange", "pink", "grey" 
size = 50

x = 0
y = 0

text = canvas.create_text(100, 100, text="Počet pokusov: 0")
text2 = canvas.create_text(133, 130, text="Počet úspešných pokusov: 0")
text3 = canvas.create_text(140, 160, text="Počet neúspešných pokusov: 0")
text4 = canvas.create_text(120, 190, text="Reakčný čas: 0")
tryes = 0
success = 0
unsuccess = 0

tickStart = 0
tickEnd = 0

def drawRandomCircle():
    global tickStart
    global circle
    global x
    global y
    
    tickStart = time.time()
    x = r.randint(0, w-50)
    y = r.randint(0, h-50)
    canvas.delete(circle)
    circle = canvas.create_rectangle(x, y, x+size, y+size, fill=r.choice(colors))

    

def onClick(event): 
    global text
    global text2
    global text3
    global text4
    global tryes
    global success
    global unsuccess

    canvas.delete(text4)
    tickEnd = time.time()
    reactionTime = tickEnd - tickStart

    if event.x > x and event.x < (x + size):
        if event.y > y and event.y < (y + size):
            circle = canvas.create_rectangle(x, y, x+size, y+size, fill="red")
            text4 = canvas.create_text(120, 190, text="Reakčný čas: " + str(reactionTime))
            success += 1
    else:
        circle = canvas.create_rectangle(x, y, x+size, y+size, fill="white")
        text4 = canvas.create_text(95, 190, text="Reakčný čas: Nan")
        unsuccess += 1

    canvas.delete(text)
    canvas.delete(text2)
    canvas.delete(text3)

    tryes += 1
    text = canvas.create_text(100, 100, text="Počet pokusov: " + str(tryes))
    text2 = canvas.create_text(133, 130, text="Počet úspešných pokusov: " + str(success))
    text3 = canvas.create_text(140, 160, text="Počet neúspešných pokusov: " + str(unsuccess))

    drawRandomCircle()
    

drawRandomCircle()
canvas.bind("<Button-1>", onClick)
canvas.mainloop()
