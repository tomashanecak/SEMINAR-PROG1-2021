import tkinter as Tk

from matplotlib.pyplot import text

w,h = 502, 500
canvas = Tk.Canvas(width=w, height=h)
canvas.pack()

numbers = [0,1,2,3,4,5,6,7,8,9]
operands = ["C", "+", "-", "="]
number = ""
operation = []
size = 50

def draw_buttons():
    x = 3
    y = h - 200
    for num in numbers:
        canvas.create_rectangle(x, y, x+size, y+size)
        canvas.create_text(x + (size/2), y + (size/2), text=str(num))
        x += size

    y += size
    x = 3
    for op in operands:
        canvas.create_rectangle(x, y, x+size, y+size)
        canvas.create_text(x + (size/2), y + (size/2), text=op)
        x += size

def draw_operation():
    canvas.delete("all")
    draw_buttons()
    canvas.create_text(50, 200, text=number, font=("Arial", 20))

def evaluate():
    global operation, number
    print(operation)
    if len(operation) > 0:
        oper = "".join(operation)
        number =  str(eval(oper))
        operation = []
        draw_operation()

def click(e):
    global number, operation
    index = e.x // size
    if e.y > 300 and e.y < 350:
        number += str(numbers[index])
    elif e.y > 350 and e.y < 400:
        operand = operands[index]
        if operand == "C":
            operation = []
            number = ""
        elif operand == "=":
            operation.append(number)
            evaluate()
        else:
            operation.append(number)
            operation.append(operand)
            number = ""
    draw_operation()
    
draw_buttons()
canvas.bind("<Button-1>", click)
canvas.mainloop()