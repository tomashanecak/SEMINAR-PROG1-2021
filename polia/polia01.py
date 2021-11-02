## Počítač generuje 20 čísiel z intervalu 1-100, vypíšte ich AP a všetky čísla väčšie ak AP
import random as r

numbers = []

for i in range(20):
    numbers.append(r.randint(1,100))

ap = sum(numbers)/len(numbers)
print(f"Počítač vygeneroval čísla {numbers}")
print(f"Ich priemer je {ap}")
print("Čísla väčšie ako AP sú: ", end=" ")

for num in numbers:
    if num > ap:
        print(num, end=", ")
