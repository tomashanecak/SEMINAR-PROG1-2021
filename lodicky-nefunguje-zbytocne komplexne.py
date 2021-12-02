import os 
import tkinter
import random

path = os.path.dirname(__file__)
file = "lodicky.txt"

canvas = tkinter.Canvas(width=700, height=600)
canvas.pack()

def drawShip():
    with open(os.path.join(path,file), "r") as map:
        num_rows = list(map.readline())[3]
        maplist = []

        for row in map:
            maplist.append(row.split(" "))
        
        mapstring = "".join(column for row in maplist for column in row)
        
        gen_row = random.randint(0, int(num_rows)-1)

        if "000" in mapstring:
            mapsubstring = "".join(maplist[gen_row])
            if "000" in mapsubstring:
                index = mapsubstring.index("000")

                for i in range(2):
                    maplist[gen_row][index + i] = 2

                drawGame()
            else:
                print("Row Full")
        else:
            print("Board Full")
    
    with open(os.path.join(path,file), "w") as map:
        
def drawGame():
    y = 50
    x = 100
    size = 50

    btn = tkinter.Button(canvas, text="Vykresli Loďku", command=drawShip)
    btn.place(x=x, y=(y-20))

    with open(os.path.join(path,file), "r") as map:
        dimensions = (map.readline()).split(" ")
        
        mapx = dimensions[0].strip()
        mapy = dimensions[1].strip()

        for row in map:
            y += size
            x = 100

            cleaned_row = row.split(" ")
            for rect in cleaned_row:
                if rect == "1":
                    color = "green"
                elif rect == "0":
                    color = "blue"
                elif rect == "2":
                    color = "red"

                canvas.create_rectangle(x, y, x+size, y+size, fill=color)
                x += size
    
def drawStatus(status):
    canvas.create_text(180,500, text = str(status), fill = "red", font=("Purisa", 12))


drawGame()
drawStatus("Všetky riadky sú voľné!")
canvas.mainloop()