import tkinter

h = 500
w = 500

canvas = tkinter.Canvas(width = str(w), height = str(h), background="black")
canvas.pack()

x = 150
y = 300

canvas.create_oval(x+50 ,y-250 ,x+150 ,y-150 , fill="white")
canvas.create_oval(x+25 ,y-150 ,x+175 ,y , fill="white")
canvas.create_oval(x ,y ,x+200 ,y+200 , fill="white")

canvas.mainloop()