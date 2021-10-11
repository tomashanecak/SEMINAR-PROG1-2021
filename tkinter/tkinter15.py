import tkinter
import random
import matplotlib

h = 500
w = 500

canvas = tkinter.Canvas(width = str(w), height = str(h), background="white")
canvas.pack()

x = w/2
y = h/2

for i in range(200):
    x2 = random.randint(10, w)
    y2 = random.randint(10, h)

    ## Takes RGB color and convert it from 1-255 range to 0-1 range 
    rgbvar1 = [x2/2, y2/2, 100]
    rgbvar2 = [x / 255.0 for x in rgbvar1]

    ##print(rgbvar2)
    ## matplotlib.colors.to_hex() converts rgb colors to HEX (!!! they must be in range 0-1 !!!)
    canvas.create_line(x, y, x2, y2, fill=str(matplotlib.colors.to_hex(rgbvar2)))

canvas.mainloop()