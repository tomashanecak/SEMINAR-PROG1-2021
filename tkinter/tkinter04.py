import tkinter as tk
import random as r

canvas = tk.Canvas(width=500,height=500)
canvas.pack()

def isEven(number):
    for i in str(number):
        if int(i) % 2 != 0:
            return 0
    return 1


for i in range(50):
    num = r.randint(1,100)
    x = r.randint(1,480)

    if isEven(i) == 0:
        y = r.randint(250,500)
        color = "red"
    else:
        y = r.randint(1,250)
        color = "green"

    canvas.create_text(x, y, text = i, fill = color)

canvas.mainloop()

    