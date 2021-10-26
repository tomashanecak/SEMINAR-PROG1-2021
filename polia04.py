## Počítač generuje 10 čísel v intervale 1-999 -> Pre každé číslo vypíšte jeho najmenšiu a najväčšiu cifru, najväačšiu cifru v čísle nahraďte hviezdičkou, skúste vypísať najčastejšie sa vyskytujúcu cifru, vypíšte vśetky čísla, v ktorých sa daná cifra nachádza
import random as r

numbers = []

def maxDigit(number):
    digits = list(str(number))
    return max(digits)

def minDigit(number):
    digits = list(str(number))
    return min(digits)

def replaceMax(number, digit):
    digits = list(str(number))

    for i, d in enumerate(digits):
        if int(d) == int(digit):
            digits[i] = "*"

    return "".join(digits)

def mostOccuring(lists):
    strings = [str(integer) for integer in lists]
    all_digits = "".join(strings)
    all_digits_arr = list(all_digits)
    all_digits_arr = [int(str) for str in all_digits_arr]
    return all_digits_arr

for i in range(10):
    num = r.randint(1,999)
    print(f"Najväčšia cifra v čísle {num} je {maxDigit(num)} a najmenšia je {minDigit(num)}")
    print(replaceMax(num, maxDigit(num)))
    numbers.append(num)

print(mostOccuring(numbers))