import tkinter as tk

w = 500
h = 500

canvas = tk.Canvas(width = w, height = h, background="black")
canvas.pack()

pyramide_width = 30
border = w//pyramide_width
block_size = (w-2*border)//pyramide_width

offset = -(block_size//2)

h_iterator = pyramide_width + 1

for i in range(pyramide_width):
    h_iterator -= 1
    offset += block_size//2

    for j in range(h_iterator):
        x = j*block_size+border+offset
        y = h-block_size*i
        x2 = j*block_size+block_size+border+offset
        y2 = h-block_size*i-block_size

        canvas.after(10)
        canvas.update()
        canvas.create_rectangle(x, y, x2, y2, fill="white", outline="black")
        
canvas.mainloop()


