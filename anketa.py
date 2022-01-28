import os
import tkinter as Tk

path = os.path.dirname(__file__)

w = 500; h = 500
canvas = Tk.Canvas(width=w, height=h)
canvas.pack()

questions = []

def load_questions():
    global questions

    with open(os.path.join(path, "anketa.txt"), "r") as file:

        for question in file:
            answers = [] 
            question = question.split(" ")
            
            answers.append(question.pop(1))
            answers.append(question.pop(1))
            answers.append(question.pop(1))

            questions.append("".join(question))

def draw_stops():
    x = 100
    y = 50
    spacing = 40

    for i, stop in enumerate(stops):
        canvas.create_text(x, y, text=stop, anchor="w")
        canvas.create_rectangle(x+150, y-(spacing/2), x+300, y+(spacing/3))
        
        percent = (stop_status[i] / max_capacity) * 100
        pixels = percent*1.5

        if percent >= 100:
            color = "red"
        else:
            color = "green"

        canvas.create_rectangle(x+150, y-(spacing/2), x+150+pixels, y+(spacing/3), fill=color)
        y += spacing

load_questions()
#draw_stops()

canvas.mainloop()