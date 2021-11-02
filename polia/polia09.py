
switch = int(input("Pre zakódovanie vety stlač 1, pre odkódovanie vety stlač 2: "))

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
    return s

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

def convert(sentence, select):
    sentence_ls = list(sentence)
    encoded_sent = ""

    for char in sentence_ls:
        if char == " ":
            encoded_sent += char
        else:
            encoded_sent += convertToSelect(ord(char), select) + "|" 
    
    return encoded_sent

def deconvert(sentence, select):
    sentence_ls = list(sentence)
    number = []
    decodedsent = ""

    for char in sentence_ls:
        if char == "|":
            decodedsent += chr(convertToDecimal(select, "".join(number)))
            number = []
        elif char == " ":
            decodedsent += " "
        else:
            number.append(char)
        
    return decodedsent
    
if switch == 1:
    sentence = str(input("Zadaj vetu: "))
    select = int(input("Zadaj do akej sústavy ju chceš zakódovať: "))
    print(convert(sentence, select))
elif switch == 2:
    sentence = str(input("Zadaj vetu: "))
    select = int(input("Zadaj v akej sústave je veta kódovaná: "))
    print(deconvert(sentence, select))

