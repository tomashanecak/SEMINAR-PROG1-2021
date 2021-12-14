def encode(n: int, plain_text: str) -> str: # vraci ciphertext typu String
    plain_text = list(plain_text)
    parts = [''.join(plain_text[i:i+n]) for i in range(0,len(plain_text),n)]

    cipher_text = ""
    for part in parts:
        cipher_text += part[::-1]
    return cipher_text

def decode(n: int, cipher_text: str) -> str: # vraci plaintext typu String
    return encode(n, cipher_text)

# Testy:
print(encode(3, "Ahoj")) # ohAj
print(encode(2, "Ahoj")) # hAjo
print(encode(10, "Ahoj")) # johA
print(encode(3, "12345")) # 32154
print(encode(5, "komunikace")) # numokecaki
print(decode(2, "hAjo")) # Ahoj
print(decode(5, "rgorpavomain")) # programovani
print(decode(3, encode(3, "Karlik a Los Karlos komunikuji sifrovane"))) # Karlik a Los Karlos komunikuji sifrovane

# na automaticke testy doporucuji assert

# def encode(n: int, plain_text: str) -> str: # vraci cyphertext typu String
#     i = 0
#     result = ""
#     while i*n <= len(plain_text):
#         start = i*n
#         end = (i+1)*n
#         result += plain_text[start:end][::-1]
#         i += 1
#     return result

# def decode(n: int, cipher_text: str) -> str: # vraci plaintext typu String
#     return encode(n, cipher_text) # jelikoz sifra je symetricka