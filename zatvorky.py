import tkinter as Tk

width, height = 500, 500
canvas = Tk.Canvas(width=width, height=height)
canvas.pack()

input = "(((2 + 3) * 12 ) - (14 * 8))"
input_arr = [x for x in input]
print(input_arr)

colors = ["blue", "red", "green", "orange", "purple"]
bracket_index_color = {}

x = 100
y = 100
bracket_index = 0

def bracket_error():
    canvas.delete("all")
    canvas.create_text(100, 100, text=input, fill="red")
    canvas.create_text(150, 150, text="Vyraz je nespravne ozatvorkovany!")

if input_arr[-1] == "(":
    bracket_error()
else:
    try:
        for char in input_arr:
            if char == "(":
                bracket_index_color[bracket_index] = colors.pop()
                canvas.create_text(x, y, text=char, fill=bracket_index_color[bracket_index])
                bracket_index += 1
            elif char == ")":
                canvas.create_text(x, y, text=char, fill=bracket_index_color[bracket_index-1])
                bracket_index -= 1
            else:
                canvas.create_text(x, y, text=char, fill="black")

            x += 5
    except:
        bracket_error()

canvas.mainloop()



