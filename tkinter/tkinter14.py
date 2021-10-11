import tkinter
import random

h = 500
w = 500

canvas = tkinter.Canvas(width = str(w), height = str(h), background="white")
canvas.pack()

for i in range(1,50):
    x = random.randint(-w/4,w)
    y = random.randint(-h/4,h)
    size = random.randint(10,300)

    colors=["black","white","yellow","blue","red","green","purple","pink","orange","magenta"]

    canvas.create_oval(x, y, x+size, y+size, fill=random.choice(colors))
    canvas.create_text(x+(size/2), y+(size/2), text=str(i)+".", fill="gray")
    canvas.after(1000)
    canvas.update()

canvas.mainloop()