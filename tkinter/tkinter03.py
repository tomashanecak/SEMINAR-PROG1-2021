import tkinter as tk
import random as r

canvas = tk.Canvas(width=500,height=500)
canvas.pack()

rang = int(input("Zadaj začiatok rozsahu čísel: "))
rangg = int(input("Zadaj koniec rozsahu čísel: "))

for i in range(rang,rangg):
    x = r.randint(10,490)
    y = r.randint(10,490)
    canvas.create_text(x,y,text=i)
    
canvas.mainloop()