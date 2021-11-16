import random
import tkinter as Tk

w = 500
h = 500

canvas = Tk.Canvas(width = w, height = h)
canvas.pack()

tipers = int(input("Zadaj počet tipujúcich: "))

tips = []
winning = []

def genRandomNumbers(arr):
    p = 0
    tip = []
    while p < 6:
        num = random.randint(1,20)
        if num not in tip:
            tip.append(num)
            p += 1
    arr.append(tip)

def checkWinner(tip, winning):
    occur = 0
    for num in tip:
        if num in winning:
            occur += 1
    return occur

genRandomNumbers(winning)
for i in range(tipers):
    genRandomNumbers(tips)

x = 50
canvas.create_text(250, x, text = f"Výherné číslo je {winning[0]}")

for tip in tips:
    x += 20
    if checkWinner(tip, winning[0]) > 2:
        color = "red"
    else:
        color= "black"
    canvas.create_text(250, x, text = tip, fill = color)
    

canvas.mainloop()





