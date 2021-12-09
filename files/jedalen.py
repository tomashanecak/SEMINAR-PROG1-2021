import tkinter as tk
import os 

path = os.path.dirname(__file__)

canvas = tk.Canvas(width=500, height=500)
canvas.pack()

entry = tk.Entry()

def drawUI():
    global entry 
    colors = ["green", "red", "blue", "orange"]
    size = 100
    x = 50
    y = 50

    for i in range(4):
        canvas.create_rectangle(x, y, x + size, y + size, fill = colors[i])
        x += 100

    entry.pack()


def createEmptyFile():
    with open(os.path.join(path, "vyber_jedla.txt"), "w") as file:
        return 1


def createLog(id, food):
    with open(os.path.join(path, "vyber_jedla.txt"), "a") as file:
        file.write(str(id) + " " + food + "\n")
        return 1


def click(e):
    size = 100
    x = 50
    foods = ["z", "c", "m", "o"]

    if e.x > 50 and e.x < 450 and e.y > 50 and e.y < 150:
        for i in range(4):
            if e.x > x and e.x < (x+size):
                print("Vybral si si: " + foods[i])

                if len(entry.get()) > 0:
                    createLog(entry.get(), foods[i])
                    drawStatus("Zapísané do databázy :)")
                else:
                    print("Error")
                    drawStatus("Nemôžem odoslař bez ID študenta!!!")

            x += size
    else:
        print("Klikol si mimo")
        drawStatus("Klikol si mimo :(")


text = canvas.create_text(250, 470, text="Zadaj ID študenta :P")
def drawStatus(status):
    global text
    canvas.delete(text)
    text = canvas.create_text(250, 470, text=status)


canvas.bind("<Button-1>", click)

drawUI()
createEmptyFile()
canvas.mainloop()