import tkinter

h = 500
w = 500

canvas = tkinter.Canvas(width = str(w), height = str(h), background="black")
canvas.pack()

y  = 0
for i in range(int(h/50)):
     canvas.create_line(0,y,w,y,fill="white")
     y += 50


canvas.mainloop()