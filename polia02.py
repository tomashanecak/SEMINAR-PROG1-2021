## Počítač generuje 10 čísiel z intervalu 5-999, nájdite najväčšie číslo a nahradte ho "MC"
import random as r

numbers = []
max = 0
index = 0

for i in range(10):
    numbers.append(r.randint(5,999))

print(f"Vygenerované čísla: {numbers}")

for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
        index = i

print(f"Najväčšie číslo je: {max}")
print(f"Jeho index je: {index}")

numbers[index] = str.upper("mc")
print(f"Nový list je: {numbers}")



