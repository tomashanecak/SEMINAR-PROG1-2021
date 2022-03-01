import os
import tkinter as Tk

path = os.path.dirname(__file__)
w, h = 500, 500
canvas = Tk.Canvas(width=w, height=h)
canvas.pack()

measurements = []
temperatures = []

with open(os.path.join(path,"meteo_stanice.txt"), "r") as db_measurements:
	for measurement in db_measurements:
		measurements.append(str(measurement))
		temperatures.append(float(measurement.strip().split(" ")[3].replace(",", ".")))
	
	canvas.create_text(100, 30, text="Pocet nacitanych merani: " + str(len(measurements)))
	for i, measurement in enumerate(measurements): canvas.create_text(115, 60 + (i * 20), text=measurement)

	canvas.create_text(80, (80 + len(measurements) * 20), text="Namerane teploty:")
	for i, temp in enumerate(temperatures): canvas.create_text(40, (100 + len(measurements) * 20) + (i * 20), text=str(temp))

	sum_temp = sum(temperatures)
	avg_temp = sum_temp / len(temperatures)
	canvas.create_text(100, (100 + len(measurements)*2 * 20), text="Priemerna teplota: " + str(round(avg_temp, 2)))
	canvas.create_text(125, (140 + len(measurements)*2 * 20), text="Najvyssia namerana teplota: " + str(max(temperatures)))

	max_temp_stations = []
	for i, measurement in enumerate(measurements):
		mes_temp = measurement.split(" ")[3].replace(",", ".")
		if mes_temp == ("+" + str(max(temperatures))):
			max_temp_stations.append(measurement.split(" ")[0])


	canvas.create_text(180, (160 + len(measurements)*2 * 20), text="Stanice s najvyssou nameranou teplotou: " + ", ".join(max_temp_stations))


canvas.mainloop()

