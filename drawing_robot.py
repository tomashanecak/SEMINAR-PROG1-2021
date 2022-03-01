import tkinter as Tk

w, h = 500, 500
canvas = Tk.Canvas(width=w, height=h)
canvas.pack()

directions = ["vlavo", "vpravo", "hore", "dole"]
direction = "vpravo"
x, y = w/2, h/2

text = canvas.create_text(100, 10, text="Aktualny smer -> vpravo")

def draw():
    global direction, x, y, text

    entry_value = (entry.get()).split(" ")
    try:
        if entry_value[0] in directions:
            direction = entry_value[0]
        elif entry_value[0] == "ciara":
            if direction == "vlavo":
                canvas.create_line(x, y, x-int(entry_value[1]), y, fill="black")
                x -= int(entry_value[1])
            elif direction == "vpravo":
                canvas.create_line(x, y, x+int(entry_value[1]), y, fill="black")
                x += int(entry_value[1])
            elif direction == "hore":
                canvas.create_line(x, y, x, y-int(entry_value[1]), fill="black")
                y -= int(entry_value[1])
            elif direction == "dole":
                canvas.create_line(x, y, x, y+int(entry_value[1]), fill="black")
                y += int(entry_value[1])
        raise Exception
    except:
        print("Neplatny prikaz!!!")
    dir_text = "Aktualny smer -> " + direction
    canvas.delete(text)
    text = canvas.create_text(100, 10, text=dir_text)

entry = Tk.Entry(canvas)
entry.place(x= w/2 - 80, y= h-100)
button = Tk.Button(canvas, text="Execute", command=draw)
button.place(x= w/2 - 42, y= h-50)

canvas.mainloop()