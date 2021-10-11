import tkinter

h = 500
w = 500

canvas = tkinter.Canvas(width = str(w), height = str(h), background="white")
canvas.pack()

num_of_rects = int(input("Zadaj veľkosť šachovnice: "))

size = h/num_of_rects
y = (-size) + 3
x = 0


for i in range(1, num_of_rects+1):
    y += size
    x = 0

    for j in range(1, num_of_rects+1):
        if( (i+j) % 2 == 0):
            color = "black"
        else:
            color = "white"

        canvas.create_rectangle(x,y,x+size,y+size, fill=color)
        x += size


canvas.mainloop()