import tkinter
import random as r

canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

colors = "red","green","blue","yellow","orange","black"

for i in range(20):
    num = r.randint(1,100)
    x = r.randint(1,450)
    y = r.randint(1,450)
    canvas.create_text(x,y,text=num,font="70",fill=r.choice(colors))

canvas.mainloop()
    
