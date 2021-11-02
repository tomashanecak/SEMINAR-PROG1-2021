## Počítač generuje čísla z intervalu 900- 99999 vypíš pôvodné číslo, číslo kde budú zotriedené cifry, súčet prvej a poslednej cifry
import random as r

numbers = []

for i in range(15):
    numbers.append(r.randint(900,99999))

# def bubbleSort(num):
#     n = len(num)

#     for i in range(n-1):
#         for j in range()

def orderDigits(numbers):
    sorted = []

    for number in numbers:
        n_str = str(number)
        n_digits = list(n_str)
        n_digits.sort()
        sorted_num = "".join(n_digits)
        sorted.append(sorted_num)
    
    return sorted

def sumOfFirstAndLast(numbers):

    for number in numbers:
        n_str = str(number)
        n_list = list(n_str)
        summ = int(n_list[0]) + int(n_list[len(n_list) - 1])
        print(f"Súčet prvej a poslednej cifry čísla {number} je {summ}")

print(numbers)
print(orderDigits(numbers))
sumOfFirstAndLast(numbers)

