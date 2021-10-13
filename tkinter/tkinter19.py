import tkinter as tk
from tkinter.font import Font
import math
import datetime

w = 500
h = w
canvas = tk.Canvas(width = w, height = h, background="gray")
canvas.pack()

size = 400
radius = size/2
center = w/2
hours = 12
angle = 360/hours

## Funkcia na premapovanie hodnôt z hodín na ulhy
def mapNum(number, rng1_end, rng2_end):
    return number * (rng2_end/rng1_end)

def generateClock():
    canvas.create_oval(center - radius, center - radius, center + radius, center + radius, fill="white", outline="gray")

    ang = 360
    for i in range(hours):
        ## Vypočítam odvesny pravouhlého trojuholníka pomocou trigonometrických funkcií
        ## Takto získam offset/vektor, ktorý musím prirátať ku originálnym súradniciam (stredu)
        ## Vynásobím * 1.09 aby boli čísla mimo kružnice

        a = radius*math.sin(math.radians(ang)) * 1.09
        b = radius*math.cos(math.radians(ang)) * 1.09

        ## sin(uhol) = protilahla/odvesna -> odbvesna*sin(uhol) = protilahla
        ## cos(uhol) = prilahla/odvesna -> odbvesna*cos(uhol) = prilahla

        canvas.create_text(center + a, center - b, text=str(12-i)+".", fill="black", font=Font(family="italic", size=20 ))

        ang -= angle

# ang = 360
# for i in range(12):
#     ang -= 30
    # canvas.create_line(center, center, center+math.sin(math.radians(360)) * radius, center-math.cos(math.radians(360)) * radius, fill="green")

while True:
    generateClock()
    ## Get Current Time 
    now = datetime.datetime.now()
    hour = now.hour # Musíme premapovať od 0 - 24 na 0 - 360
    minute = now.minute # Musíme premapovať od 0 - 60 na 0 - 360
    second = now.second # Musíme premapovať od 0 - 60 na 0 - 360

    print(f"Aktuálna hodina je: {hour} čo je -> {mapNum(hour,24,360)} stupňov")
    print(f"Aktuálna minúta je: {minute} čo je -> {mapNum(minute,60,360)} stupňov")
    print(f"Aktuálna sekunda je: {second} čo je -> {mapNum(second,60,360)} stupňov")

    secondAng = mapNum(second, 60, 360)
    minuteAng = mapNum(minute, 60, 360)
    hourAng = mapNum(hour, 24, 360)

    canvas.create_line(center, center, center+(math.sin(math.radians(secondAng)) * radius) * 0.7, center-(math.cos(math.radians(secondAng)) * radius) * 0.7, fill="green")
    canvas.create_line(center, center, center+(math.sin(math.radians(minuteAng)) * radius) * 0.8, center-(math.cos(math.radians(minuteAng)) * radius) * 0.8, fill="blue")
    canvas.create_line(center, center, center+(math.sin(math.radians(hourAng)) * radius) * 0.9, center-(math.cos(math.radians(hourAng)) * radius) * 0.9, fill="red")

    canvas.after(2000)
    canvas.update()

canvas.mainloop()
    
