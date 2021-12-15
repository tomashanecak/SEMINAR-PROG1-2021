import os 

path = os.path.dirname(__file__)

key = [" ", "ABC" ,"DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]

def encode(plaintext):
    plntxt_chars = list(plaintext)
    plntxt_chars = [char.upper() for char in plntxt_chars]
    print(plntxt_chars)
    cyphertxt_chars = []

    for char in plntxt_chars:
        for i in range(len(key)):
            if char in key[i]:
                sub_index = key[i].find(char)
                for j in range(sub_index + 1):
                    cyphertxt_chars.append(str(i))
                cyphertxt_chars.append(" ")
            elif (char.isalpha() == False) and (char != '\n') and (char != " "):
                raise Exception("Neviem spracovať iné znaky ako písmená od A-Z, a-z a medzery :(")
    
    return "".join(cyphertxt_chars)

def decode(cyphertext):
    cyphertxt_chars = cyphertext.split(" ")
    cyphertxt_chars.pop()
    plntxt_chars = []

    for number in cyphertxt_chars:
        count = number.count(number[0])
        plntxt_chars.append(key[int(number[0])][int(count)-1])

    return "".join(plntxt_chars)


with open(os.path.join(path, "sifrovat_text.txt"), "r") as plaintextfile:
    plaintext_arr = []
    cyphertext_arr = []

    for row in plaintextfile:
        cyphertext_arr.append(encode(row))

    for c in cyphertext_arr:
        print(c)
        plaintext_arr.append(decode(c))
    
    for p in plaintext_arr:
        print(p)
        


