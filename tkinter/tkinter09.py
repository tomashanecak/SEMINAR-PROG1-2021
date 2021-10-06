import tkinter

h = 500
w = 500

canvas = tkinter.Canvas(width = str(w), height = str(h), background="black")
canvas.pack()

x = 50
size = 50
# x = int(input("Select starting point: "))
y = x
#size = int(input("Select size: "))


#canvas.create_line(x,y,x+size,y,x+size,y+size,x,y+size,x,y, fill="white")
canvas.create_line(x,y,x+150,y,x+150,y+50,x,y+50,x,y, fill="blue", width=10)

canvas.mainloop()