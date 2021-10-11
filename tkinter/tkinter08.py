import tkinter

h = 500
w = 500

canvas = tkinter.Canvas(width = str(w), height = str(h), background="black")
canvas.pack()

canvas.create_line(250,100,350,200,150,200,250,100, fill="white")

canvas.mainloop()