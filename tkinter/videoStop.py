import tkinter as tk
import random as r
from typing import Text

w = 500
h = w
canvas =tk.Canvas(width = w, height = h, background="white")
canvas.pack()

x = 125
y = 200
offset = 0
state = "Start"
numbers = [0, 0, 0]
score = 20

# def drawMessage(message, color):
#     canvas.create_text(100, 110, text=message, fill=color)

def drawGame():
    global offset

    canvas.delete("all")
    canvas.create_text(100, 100, text="Tvoje skóre je: " + str(score))

    for i, number in enumerate(numbers):
            numbers[i] = r.randint(1,6)

    for i in range(3):
        canvas.create_rectangle(x+offset,y,x+offset+50,y+50, fill="green")
        canvas.create_text(x+offset + 25, y+25, fill="white", text=numbers[i])
        offset += 100
    offset = 0

    canvas.after(1000)
    canvas.update()
    gameTrigger()
    
def checkNumbers():
    global numbers 
    global score

    print(f"Čísla sú: {numbers}")
    canvas.delete("all")
    canvas.create_text(100, 100, text="Tvoje skóre je: " + str(score))

    if numbers[0] == numbers[1] == numbers[2]:
        score += 5
    elif numbers[0] != numbers[1] != numbers[2]:
        score -= 2
    else:
        score += 2

def gameTrigger():
    global state
    global numbers
    global loopState

    if state == "Stop":
        drawButton()
        drawGame()  
    else:
        drawButton()
        checkNumbers()

def changeState():
    global state 

    if state == "Start":
        state = "Stop" 
        gameTrigger()
    elif state == "Stop":
        state = "Start"
        gameTrigger()

btn =tk.Button(canvas, text=state, command=changeState).place(x = 218, y = 300)
def drawButton():
    global btn
    canvas.delete(btn)
    btn =tk.Button(canvas, text=state, command=changeState).place(x = 218, y = 300)

drawButton()
canvas.mainloop()


