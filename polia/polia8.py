# Program, ktorý prevedie akékoľvek číslo z 10 sústavy do akejkoľvek zadanej

switch = int(input("AK chceš konvertovať z 10kovej stlač 1 ak chceš konvertovať do 10kovej stlač 2: "))

def convertToSelect(number, select):
    rests = []
    n = number
    while n != 0:
        rest = n%select

        d = {
            10 : "A",
            11 : "B",
            12 : "C",
            13 : "D",
            14 : "E",
            15 : "F",
        }

        if rest > 9:
            rests.append(d[rest])
        else:
            rests.append(rest)

        n = n//select

    rests.reverse()
    s = ''.join(map(str, rests))
    return int(s)

def convertToDecimal(select, number):
    summ = 0
    number = list(str(number))

    if select > 10:
        d = {
                "A" : 10,
                "B" : 11,
                "C" : 12,
                "D" : 13,
                "E" : 14,
                "F" : 15,   
            }

        for i, el in enumerate(number):
            if el in d:
                number[i] = d[el]

    number.reverse()

    for i, n in enumerate(number):
        summ += (int(n)*(select**i))

    return summ

if switch == 1:
    number = int(input("ZADAJ ČÍSLO KTORÉ CHCEŠ KONVERTOVAŤ: "))
    select = int(input("Zadaj sústavu, do ktorej chceš previesť: "))
    print(convertToSelect(number,select))
elif switch == 2:
    select = int(input("Zadaj sústavu, z ktorej chceš previesť: "))
    number = input("ZADAJ ČÍSLO KTORÉ CHCEŠ KONVERTOVAŤ: ")
    print(convertToDecimal(select, number))





    



