import os

key = "totojesupermegasifrovacikluc"

def keyToNumber(key):
    key_chars = list(key)
    key_nums = []

    for char in key_chars:
        key_nums.append(ord(char) - 96)
    
    return key_nums

def encrypt(key, txt):
    index = 1
    encrypted = []

    for row in txt:
        for char in row:

            shift = ord(char.lower()) + index
            if shift > 122:
                shift -= 26

            encrypted.append(chr(shift))

            if index == (len(key)):
                index = 1
            else:
                index += 1

    return "".join(encrypted)


def decrypt(key, txt):
    index = 1
    decrypted = []

    for row in txt:
        for char in row:

            shift = ord(char) - index
            if shift < 97:
                shift += 26
            if shift == 58:
                shift = 32
                
            decrypted.append(chr(shift))

            if index == (len(key)):
                index = 1
            else:
                index += 1

    return "".join(decrypted)

def inputOutputSystem():
    with open("sifrovat_text.txt", "r") as decryptedtxt:

        # Funguje aj s niekoľko riadkovými súbormi, preto je tu tento cyklus :)
        txt = []
        for row in decryptedtxt:
            txt.append(row)
        
        enc = encrypt(keyToNumber(key), txt)
        dec = decrypt(keyToNumber(key), enc)

        print(f"Originálny text: {txt} ")
        print(f"Zašifrovaný text {enc} ")
        print(f"Rozšifrovaný text: {dec}")
        print("--- SIFROVANY TEXT BOL ZAPISANY DO SUBORU ---")
    
    with open("nova_sifra.txt", "w") as encryptedtxt:
        print(enc, file=encryptedtxt)
    
inputOutputSystem()