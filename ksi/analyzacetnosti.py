# Tuto funkci implementuj. Smaz prikaz 'pass' a pis telo funkce.
def word_frequency(text):
    dict = {}

    words = getwords(text)
    for word in words:
        word = word.lower()
        if word == "":
            pass
        elif word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    
    return dict

def getwords(str):
    words = []
    for char in str:
        if char.isalpha():
            words.append(char)
        elif len(words) > 1:
            if words[-1] != "x":
                words.append("x")
    w = "".join(words)
    return w.split("x")
        

# testy (upravujte dle libosti)
print(word_frequency("Ksi, Ksa, Ksi, Kse"))       # {'ksi': 2, 'ksa': 1, 'kse': 1}
print(word_frequency("Ksi,+Ksa,Ksi;;-;Kse_"))     # {'ksi': 2, 'ksa': 1, 'kse': 1}
print(word_frequency("Informatika je nejlepsi"))  # {'informatika': 1, 'je': 1, 'nejlepsi': 1}

# def word_frequency(text):
#     # prevod textu na mala pismena
#     text = text.lower()

#     # nahrazeni vsech oddelovacu mezerami
#     nice_text = ''
#     for c in text:
#         if c.isalpha():
#             nice_text += c
#         else:
#             nice_text += ' '

#     # rozdeleni textu na jednotliva slova
#     words = nice_text.split()

# # spocitame pocet vyskytu kazdeho slova do slovniku freqs
#     freqs = {}
#     for word in words:
#         freqs[word] = freqs.get(word, 0) + 1
#     # vratime vysledek
#     return freqs