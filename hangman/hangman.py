import os
import random as r
import tkinter as Tk
from tkinter.ttk import Button, Entry

w, h = 500, 500
canvas= Tk.Canvas(width=w,height=h)
canvas.pack()

words = ["bicykel", "kolobezka", "skejt", "auto", "lyze", "desafortunadamente"]
word = ""
guessed = ""

y = 100
size = 20

def startGame():
    global word
    word = r.choice(words)
    print(word)
    word = list(word)

    x = 20
    for i in range(len(word)):
        canvas.create_line(x, y, x+size,y)
        x += size + 5

entry = Tk.Entry()
entry.place(x=200, y=450)
def sendWord():
    global guessed
    letter = entry.get()

    if len(letter) == 0:
        print("Error empty input")
        return
    elif len(letter) > 1:
        print("Error -> Put just one letter at a time")
        return
    
    if not (letter in word):
        print("Not in word")
    elif letter in guessed:
        print("Already guessed")
    else:
        guessed += letter

        for index, char in enumerate(word):
            if char == letter:
                x = ((index+1) * 20) + (index*5) + 10
                canvas.create_text(x,y-10, text=letter)
                
startGame()
button = Tk.Button(canvas, text="Send", command=sendWord).place(x=400, y=450)


canvas.mainloop()