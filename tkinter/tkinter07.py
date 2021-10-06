import tkinter

h = 500
w = 500

canvas = tkinter.Canvas(width = str(w), height = str(h), background="black")
canvas.pack()

inclination = float(input("Zadajte inklináciu: "))

x1 = 250
x2 = 251
y = 1
for i in range(500):
    canvas.create_line(x1,y,x2,y, fill="white")
    x1 -= inclination
    x2 += inclination
    y += 1

canvas.mainloop()