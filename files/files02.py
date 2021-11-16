# Zadajte meno existujúceho súboru, pre každý riadok vypíšte poćet samohlások a na konci vypíšte koľko samohlások v súbore bolo dokopy

import os
path = os.path.dirname(__file__)
name = ""

count_total = [0, 0, 0, 0, 0, 0]

def countVowels(row):
    global count_total
    char_arr = list(row)
    count = [0 ,0 ,0 ,0 ,0 ,0]

    count[0] = char_arr.count("a") + char_arr.count("A")
    count[1] = char_arr.count("e") + char_arr.count("E")
    count[2] = char_arr.count("y") + char_arr.count("Y")
    count[3] = char_arr.count("o") + char_arr.count("O")
    count[4] = char_arr.count("u") + char_arr.count("U")
    count[5] = char_arr.count("y") + char_arr.count("Y")

    count_total = [a+b for a, b in zip(count, count_total)]
    return count

def countVowelsTotal(count):
    return sum(count)

while name == "":
    name = str(input("Zadaj názov súboru: "))

with open(os.path.join(path, name + ".txt"), "r") as f:
    for row in f:
        print(f"{row} -> V tejto vete je {countVowelsTotal(countVowels(row))} samohlások!")

print("------------------------------")
vowels = ["A", "E", "I", "O", "U", "Y"]
print(tuple(zip(vowels, count_total)))