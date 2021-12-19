from flask import Flask, jsonify, redirect, url_for, render_template
import requests
import json

app = Flask("SmartHome", template_folder='template')

motion_sensors_ids = []
smart_lights_ids = []
switch_sensors_ids = []
owners = ["Sob Karlos", "Jelen Martin", "Sova Eliska", "Spolocné", "Spolocné"]

# Na úlohe som žiaľ začal pracovať príliš neskoro, posielam aspoň to málo, čo som stihol :(
# Snáď je to worth aspoň 1/2 bodíky :PP
# Tomáš Hanečák

for i in range(5):
    motion_sensor = requests.get("http://home_automation.iamroot.eu/newMotionSensor")
    motion_sensor_info =  motion_sensor.json()
    motion_sensors_ids.append(motion_sensor_info["actions"]["device_info"].rsplit('/', 1)[-1])

for i in range(5):
    smart_light = requests.get("http://home_automation.iamroot.eu/newSmartLight")
    smart_light_info =  smart_light.json()
    smart_lights_ids.append(smart_light_info["actions"]["device_info"].rsplit('/', 1)[-1]) 

for i in range(5):
    switch_sensor = requests.get("http://home_automation.iamroot.eu/newSwitchSensor")
    switch_sensor_info =  switch_sensor.json()
    switch_sensors_ids.append(switch_sensor_info["actions"]["device_info"].rsplit('/', 1)[-1])

for i in range(5):
    requests.post(f"http://home_automation.iamroot.eu/device/{smart_lights_ids[i]}/notes", data=f"{owners[i]}")

@app.route("/")
def index():
    smart_lights_states = []
    smart_lights_tempreratures = []
    smart_lights_usages = []
    smart_lights_owners = []
    total_usage = 0
    for id in smart_lights_ids:
        state = requests.get(f"http://home_automation.iamroot.eu/device/{id}")
        data = state.json()
        smart_lights_states.append(data["current_state"])
        smart_lights_tempreratures.append(data["color_temperature"])
        smart_lights_usages.append(data["power_usage"])
        total_usage += data["power_usage"]
        smart_lights_owners.append(data["notes"])

    return render_template("index.html", light_ids = smart_lights_ids, light_states = smart_lights_states, light_temperatures = smart_lights_tempreratures, light_usages = smart_lights_usages, total_usage = total_usage, owners = smart_lights_owners)



    
