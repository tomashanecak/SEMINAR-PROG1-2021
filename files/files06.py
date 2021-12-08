## Zadajte meno vstupného súboru, ak neexistuje tak načítajte doňho 5 viet a keď existuje, vypíšete z daného súboru vetu, ktorá má najviac slov
import os 
path = os.path.dirname(__file__)

file = ""

def new_file(file_name):
    file = open(os.path.join(path, file_name), "w")

    for i in range(5):
        inp = input("Zadaj riadok")
        print(inp, file=file)
        
    file.close()

def open_file():
    global file 

    try:
        file_name = input("Zadaj nazov súboru: ")
        file = open(os.path.join(path, file_name), "r")
    except:
        print("Súbor neexistuje!")
        print("Chcete vytvoriť nový súbor? [A/N] Áno/Nie?")
        new_switch = str(input("[A/N] Áno/Nie?"))

        if new_switch == "A":
            new_file(file_name)
        else:
            open_file()

open_file()

longest = ""
max_len = 0

for i, file in enumerate(file):
    print(f"{i+1}. {file}")
    count = 0
    is_space = False

    for char in file:
        if is_space == False and char == " ":
            count += 1

        if char == " ":
            is_space = True
        else: 
            is_space = False
        
    if count>max_len: 
        max_len = count
        longest = file


print(f"Najdlhšia veta je veta -> {longest} s počtom slov {max_len + 1}")