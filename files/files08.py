"""
Počítačová hra je tvorená generovaním N náhodných čísiel, ktoré sú trojciferné. Tieto čísla sa ukladajú do textového súboru generovane_cisla.txt po 5 v jednom riadku. Následne hráč vkladá číselnú hodnotu z intervalu od 1 po 27. Program vyhodnocuje, koľko trojciferných čísiel, vygenerovaných na začiatku hry, má ciferný súčet zhodný s číselnou hodnotou vloženou hráčom. Cena hry je daná práve počtom týchto zhôd.
Vytvorte program pre takto definovanú hru, ktorý:
- vypíše vygenerované čísla zo súboru,
- vyhodnotí hru a vypíše cenu hry.

"""

import os 
import random 

path = os.path.dirname(__file__)

filename = "generovane_cisla.txt"
player_value = ""

with open(os.path.join(path+"\\"+filename), "w") as file:
    for i in range(10):
        if i != 0: print("\n", file = file)
        for j in range(5):
            print(random.randint(100,999), file = file, end = " ")

def p_input():
    global player_value
    player_value = int(input("Zadaj číslo od 0-27: "))

    if player_value > 27 or player_value < 0:
        print("Hodnota musí byť v intervale 0-27!!!")
        p_input()

p_input()

print("Generované čísla: ")

with open(os.path.join(path+"\\"+filename), "r") as file:
    arr_digit_sums = []

    for row in file:
        numbers = row.split(" ")
        numbers.pop()

        for number in numbers:
            print(number , end = "|")
            digit_sum = int(number[0]) + int(number[1]) + int(number[2])
            arr_digit_sums.append(digit_sum)

print("\n----------------------------------------------")
num_of_occurencies = arr_digit_sums.count(player_value)
print(f"Počet výskytov hodnoty je {num_of_occurencies}")
print("----------------------------------------------")

if num_of_occurencies == 0:
    print("Je mi ľúto, nič si nevyhral :(")
elif num_of_occurencies > 0 and num_of_occurencies < 3:
    print("Vyhrávaš Bronzovú cenu!")
elif num_of_occurencies > 3 and num_of_occurencies < 5:
    print("Vyhrávaš Striebornú cenu!")
elif num_of_occurencies > 5:
    print("Vyhrávaš Zlatú cenu!")