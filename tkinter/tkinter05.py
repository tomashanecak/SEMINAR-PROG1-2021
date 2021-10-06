## Absolutne zle som pochopil zadanie a nikto nevie ako to funguje ale nejako to funguje XDDDD
## Ineficcient yet working
import tkinter as tk
import random as r

canvas = tk.Canvas(width=1000,height=800)
canvas.pack()

def checkAscending(num1, num2, switch):
    if switch == 0:
        if num1 < num2:
            return 1
        else:
            return 0
    elif switch == 1:
        if num2 < num1:
            return 1
        else:
            return 0

rnd1 = r.randint(10, 10000)
rnd2 = r.randint(10, 10000)
x = 100
y = 20
switch = 0
canvas.create_text(x, y, text=rnd1, fill="red", font=("italic", 20))


for i in range(40):
    if checkAscending(rnd1, rnd2, switch) == 1:
        x += 100

        if switch == 0:
            canvas.create_text(x, y, text=rnd2, fill="green", font=("italic", 20))
        else:
            canvas.create_text(x, y, text=rnd1, fill="green", font=("italic", 20))
    else:
        x = 100
        y += 35

        if switch == 0:
            canvas.create_text(x, y, text=rnd2, fill="red", font=("italic", 20))
        else:
            canvas.create_text(x, y, text=rnd1, fill="red", font=("italic", 20))

    if switch == 0:
        rnd1 = r.randint(10, 10000)
        switch = 1
    else:
        rnd2 = r.randint(10, 10000)
        switch = 0


canvas.mainloop()

