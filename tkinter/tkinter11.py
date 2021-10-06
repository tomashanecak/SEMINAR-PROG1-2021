import tkinter

h = 500
w = 500

canvas = tkinter.Canvas(width = str(w), height = str(h), background="white")
canvas.pack()

z1 = 250
z2 = 250
offset = 250


for i in range(5):
    if i % 2 == 0:
        color = "black"
    else:
        color = "white"

    canvas.create_oval(z1+offset, z2+offset, z1-offset, z2-offset, fill=color)
    offset -= 50


canvas.mainloop()