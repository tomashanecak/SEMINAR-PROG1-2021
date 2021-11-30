## Zadajte meno vstupného súboru až kým ho nezadáme správne, vypíšte daný súbor (enumerate rows) na konci vypíšte, ktorý riadok bol najdlhší
import os
path = os.path.dirname(__file__)

file = ""

def open_file():
    global file
    try:
        file_name = input("Zadaj názov súboru: ")
        file = open(os.path.join(path, file_name), "r")
    except:
        print("File was not found :( Try Again")
        open_file()

open_file()

longest = ""
max_len = 0

for i, file in enumerate(file):
    print(f"{i+1}. {file}")

    if len(file) > max_len:
        max_len = len(file)
        longest = file

print(f"Najdlhšia veta je veta -> {longest} s dĺžkou {max_len} znakov")

