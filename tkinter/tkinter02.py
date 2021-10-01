import tkinter as tk

canvas = tk.Canvas(width=500,height=500)
canvas.pack()

y = 20
x = 10

for i in range(30):
    
    canvas.create_text(x,y,text=i)
    x += 50

    if x > 480:
        y += 20
        x = 10

canvas.mainloop()


