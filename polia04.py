# Počítač generuje 10 čísel v intervale 1-999 -> Pre každé číslo vypíšte jeho najmenšiu a najväčšiu cifru, najväačšiu cifru v čísle nahraďte hviezdičkou, skúste vypísať najčastejšie sa vyskytujúcu cifru, vypíšte vśetky čísla, v ktorých sa daná cifra nachádza
import random as r
from typing import Counter

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


def countOccurencies(digits_arr: list):
    digits_count = []

    for i in range(10):
        digits_count.append(digits_arr.count(i))

    return digits_count


def mostOccuring(lists):
    strings = [str(integer) for integer in lists]
    all_digits = "".join(strings)
    all_digits_arr = list(all_digits)
    all_digits_arr = [int(str) for str in all_digits_arr]
    print(f"All digits: {all_digits_arr}")

    digits_count = countOccurencies(all_digits_arr)
    print(f"Occurencies of each digit: {digits_count}")
    num_occur = max(digits_count)
    most_occuring = []

    for i in range(len(digits_count)):
        if digits_count[i] == num_occur:
            most_occuring.append(i)

    print(f"Number of occurencies {num_occur}")
    print(f"Most occuring: {most_occuring}")

    return most_occuring

def printAllWithMostOccuring(most_occuring):
    cont_most_occuring = []

    for number in numbers:
        for d in most_occuring:
            if str(d) in str(number):
                cont_most_occuring.append(number)

    return list(dict.fromkeys(cont_most_occuring))


for i in range(10):
    num = r.randint(1, 999)
    print(
        f"Najväčšia cifra v čísle {num} je {maxDigit(num)} a najmenšia je {minDigit(num)}")
    print(replaceMax(num, maxDigit(num)))
    numbers.append(num)


print(f"Numbers that contain most occuring: {printAllWithMostOccuring(mostOccuring(numbers))}")
