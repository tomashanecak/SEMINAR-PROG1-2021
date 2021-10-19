import tkinter as tk
from tkinter.constants import ANCHOR, NW

canvas = tk.Canvas(width = 500, height = 500)
canvas.pack()

img = tk.PhotoImage(file="/Users/tomashanecak/Downloads/13.10.2021/campus.png")
img = img.subsample(2, 2)
canvas.create_image(0, 0, image=img)
canvas.mainloop()