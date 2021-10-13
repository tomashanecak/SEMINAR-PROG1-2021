import tkinter as tk
import random as r

w = 500
h = 500
canvas = tk.Canvas(width = w, height = h, background="black")

canvas.pack()

num_of_bars = 10
border = w//num_of_bars
bar_width = (w-2*border)//num_of_bars

for i in range(num_of_bars):
    color = f"#{r.randrange(255**3):06x}"
    canvas.create_rectangle(i*bar_width+border, h, i*bar_width+bar_width+border, h-((i+1)*bar_width), fill=color, outline="white")
    canvas.create_text(i*bar_width+border+bar_width//2, h-((i+1)*bar_width)//2, text=str(i+1)+".", fill="white")

    canvas.after(100)
    canvas.update()

    
canvas.mainloop()

