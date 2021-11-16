import random as r
import tkinter as tk

w = 1002
h = 500

canvas = tk.Canvas(width = w, height = h)
canvas.pack()

binary = []
compressed_binary = []
row = []
size = 250

def generateBinary():
    global row
    for i in range(size):
        if len(row) > 0: binary.append(row)
        row = []
        for j in range(size):
            row.append(r.randint(0,1))

def drawBinary():
    x = 502
    y = -2
    for byte in binary:
        y+=2
        x=502
        for b in byte:
            color = "black" if b == 1 else "white"
            canvas.create_rectangle(x,y,x+2,y+2, fill = color)
            x+=2

def compress(binary):
    compressed = []
    for byte in binary:
        count = 0
        row = []

        if byte[0] == 1:
            row.append(0)
            looking_for = 1
        else:
            looking_for = 0
            
        for b in byte:
            if b == looking_for:
                count += 1
            else:
                row.append(count)
                looking_for = b
                count = 1

        row.append(count)
        compressed.append(row)
    
    return compressed

def drawCompressed(compressed):
    x = 0
    y = -2
    switch = -1

    for row in compressed:
        x = 0
        y += 2
        for r in row:
            color = "black" if switch == -1 else "white"
            for i in range(r):
                canvas.create_rectangle(x,y,x+2,y+2, fill = color)
                x+=2
            switch *= -1

    

generateBinary()
drawBinary()

compressed_binary = compress(binary)
for b in compressed_binary:
    print(b)

drawCompressed(compressed_binary)

canvas.mainloop()