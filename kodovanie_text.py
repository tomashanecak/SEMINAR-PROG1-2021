sent = str(input("Zadaj vetu: "))

ascii_chars = []
bin_ascii_chars = []

for char in sent:
    ascii_chars.append(ord(char))

def dec_to_bin(number):
    rest = number % 2
    division = number // 2
    result = [rest]
    while division != 0:
        rest = division % 2
        division = division // 2
        result.append(str(rest))
    result.reverse()
    return "".join(str(rest))

def dec_to_hex(number):
    rest = number % 16
    division = number // 16
    result = [rest]
    while division != 0:
        rest = division % 2
        division = division // 2
        result.append(str(rest))
    result.reverse()
    return "".join(str(rest))

for num in ascii_chars:
    print(dec_to_bin(num))


    



# print(ascii_chars)