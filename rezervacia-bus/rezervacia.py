import tkinter as Tk
import os

path = os.path.dirname(__file__)

canvas = Tk.Canvas(width = 600, height=500)
canvas.pack()

class Bus:
	def __init__(self, path, file, length, canvas):
		self.path = path
		self.file = file
		self.length = length
		self.canvas = canvas
		self.bus_map = []
		self.bus_map_blank = []
		self.size = 50
	
	def new_bus(self):
		with open(os.path.join(self.path, self.file), "w") as bus:
			self.bus_generator(bus, True)
			
	def bus_generator(self, file=None, write = True):
		for i in range(1,5):
				row = []
				x = i
				row.append(i)
				for j in range(1, self.length):
					x += 4
					row.append(x)
				if write == True:
					print(row, file=file)
				self.bus_map_blank.append(row)
	
	def load_bus(self):
		with open(os.path.join(self.path, self.file), "r") as bus:
			bus_map = []
			for row in bus:
				bus_row = row.strip("[]\n''")
				bus_row = bus_row.split(",")
				bus_map.append(bus_row)
			self.bus_map = bus_map

	def draw_bus(self):
		print(self.bus_map)
		x = 50
		y = 50
		for row in self.bus_map:
			y += self.size
			x = 50
			for chair in row:
				color = "red" if str(chair) == "X" else "green"
				self.canvas.create_rectangle(x, y, x+self.size, y+self.size, fill=color)
				self.canvas.create_text(x+self.size/2, y+self.size/2, text=chair.strip("'"))
				x+=self.size
	
	def click(self, e):
		x = ((e.x - 50)//self.size)
		y = ((e.y - 300)//self.size)

		# print(x)
		# print(y)
		# print(e.x)
		# print(e.y)
		# print(self.bus_map[y][x])
		# print(self.bus_map)

		if self.bus_map[y][x] != "X":
			self.bus_map[y][x] = "X"
		else:
			self.bus_map[y][x] =  str(self.bus_map_blank[y][x])
		
		print(self.bus_map_blank)
		self.draw_bus()
	
	def save_bus(self):
		with open(os.path.join(self.path, self.file), "w") as bus:
			for i, row in enumerate(self.bus_map):
				for j, chair in enumerate(row):
					try:
						self.bus_map[i][j] = int(chair)
					except:
						print("Not an integer")
				print(row, file=bus)
			print(self.bus_map)

bus = Bus(path, "autobus.txt", 10, canvas)
# bus.new_bus()
bus.bus_generator(None, False)
bus.load_bus()
bus.draw_bus()

canvas.bind("<Button-1>", bus.click)
new_btn = Tk.Button(canvas, text="Save", command=bus.save_bus)
new_btn.place(x=50,y=450)

canvas.mainloop()



