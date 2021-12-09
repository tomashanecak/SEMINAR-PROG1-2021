import os 
import tkinter
import random

path = os.path.dirname(__file__)
file = "lodicky.txt"

canvas = tkinter.Canvas(width=700, height=600)
canvas.pack()

map = []
num_rows = 0
text = canvas.create_text(180,500, text = "Prístav je prázdny!", fill = "red", font=("Purisa", 12))

def drawShip():
    global map

    maplist = []
    for row in map:
        maplist.append(row.split(" "))
        
    mapstring = "".join(column for row in maplist for column in row)
        
    gen_row = random.randint(0, int(num_rows)-1)

    if "000" in mapstring:
        mapsubstring = "".join(maplist[gen_row])
        print(mapsubstring)
        if "000" in mapsubstring:
            index = mapsubstring.index("000")
            print("Generated row: " + str(gen_row) + " Found index: " + str(index))

            for i in range(3):
                maplist[gen_row][index + i] = "2"

            map[gen_row] = " ".join(maplist[gen_row])

            drawGame()
        else:
            print("Row Full")
    else:
        print("Board Full")
        drawStatus("Prístav je plný!!!")
    
    print(map)

def getGameData():
    global map
    global num_rows

    with open(os.path.join(path,file), "r") as mapfile:
        dimensions = (mapfile.readline()).split(" ")
        num_rows = dimensions[1].strip()

        for row in mapfile:
            map.append(row)

        
def drawGame():
    y = 50
    x = 100
    size = 50

    for row in map:
        y += size
        x = 100

        cleaned_row = row.split(" ")
        for rect in cleaned_row:
            if rect == "1" or rect == "1\n":
                color = "green"
            elif rect == "0" or rect == "0\n":
                color = "blue"
            elif rect == "2" or rect == "2\n":
                color = "red"

            canvas.create_rectangle(x, y, x+size, y+size, fill=color)
            x += size
    
def drawStatus(status):
    global text
    canvas.delete(text)
    text = canvas.create_text(180,500, text = str(status), fill = "red", font=("Purisa", 12))
    


getGameData()
drawGame()

btn = tkinter.Button(canvas, text="Vykresli Loďku", command=drawShip)
btn.place(x=100, y=30)


canvas.mainloop()