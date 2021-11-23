import os
import tkinter as Tk

w = 500
h = 500
canvas = Tk.Canvas(width = w, height = h)
canvas.pack()

path = os.path.dirname(__file__)
filename = "vyska.txt"
number_in_class = dict()

with open(os.path.join(path, filename), "r") as file:
    for row in file:
        row_list = row.split(" ")
        if row_list[1] in number_in_class:
            number_in_class[row_list[1]].append(row_list[0])
        else: 
            number_in_class[row_list[1]] = [row_list[0]]
            
sort_in_class = sorted(number_in_class.items(), key=lambda x: x[1])

x = 100
y = 50
for n in sort_in_class:
    print(n[0], " -> ", len(n[1]))

    canvas.create_text(x, y, text=n[0])
    y += 15

    for i in range(len(n[1])):
        canvas.create_text(x, y, text=n[1][i])
        y += 15

canvas.mainloop()

