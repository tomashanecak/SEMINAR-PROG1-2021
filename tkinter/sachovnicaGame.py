import tkinter as tk

w = 500
h = 600
canvas = tk.Canvas(width=w, height=h, background="white")
canvas.pack()


size = w / 11
char_offset = 0
num_offset = 0

pis = canvas.create_text(100, 550, text="")


def onClick(event):
    global pis
    canvas.delete(pis)
    x_cord = int(event.x//size) - 1
    y_cord = int(event.y//size) - 1

    x_txt = str(chr(65 + x_cord))
    y_txt = str(chr(48 + y_cord))

    text = "Klikol si na pole: " + x_txt + y_txt
    pis = canvas.create_text(100, 550, text=text)

    print(x_cord, y_cord)

for i in range(11):
    for j in range(11):
        x = j*size 
        y = i*size 
        canvas.create_rectangle(x, y, x + size, y + size)

        if i == 0 and x > 0:
            canvas.create_text(x + size/2, y + size/2, text = str(chr(65 + char_offset)))
            char_offset += 1
        elif x == 0 and y > 0: 
            canvas.create_text(x + size/2, y + size/2, text = str(chr(48 + num_offset)))
            num_offset += 1

canvas.bind("<Button-1>", onClick)

canvas.mainloop()