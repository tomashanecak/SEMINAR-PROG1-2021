import tkinter

h = 500
w = 500

canvas = tkinter.Canvas(width = str(w), height = str(h), background="white")
canvas.pack()

# pk = int(input("Zadaj počet kruhov: "))

##Draws desired number of bw circles
def drawCircles(num_circles):
    z1 = 250
    z2 = 250

    ##Tweak this value to change distance from the edge :)
    offset = 240 #//pk
    calc_offset = offset/num_circles

    circle_id = 1

    for i in range(num_circles):
        colors = ["black","white"]
        if i % 2 == 0:
            oval_clr_id = 0
            txt_clr_id = 1
        else:
            oval_clr_id = 1
            txt_clr_id = 0

        canvas.create_oval(z1+offset, z2+offset, z1-offset, z2-offset, fill=colors[oval_clr_id])

        if(i == (num_circles-1)):
            canvas.create_text(z1, z2, text=str(circle_id)+".", fill=colors[txt_clr_id])
        else:
            canvas.create_text(z1-(offset-calc_offset/2), z2, text=str(circle_id)+".", fill=colors[txt_clr_id])

        ##Sets timeout between drawing
        canvas.after(1000)
        canvas.update()

        ##Calculates new offset and increments circle id 
        offset -= calc_offset
        circle_id += 1

drawCircles(int(input("Zadaj počet kruhov: ")))
canvas.mainloop()