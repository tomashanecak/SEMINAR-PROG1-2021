## Vstupujú vety, kým nevstúpi prázdna veta, vytlačte priemerný počet slov v jednej vete, vytlačte všetky vety, kde je počet slov väčší ako priemerný

run = True
sentences = []

while run == True:
    inpt = str(input("Zadaj vetu alebo enter, pre štart programu: "))

    if inpt != "":
        sentences.append(inpt)
    else:
        run = False
        break

def avgWords(sentences):
    words_count = []

    for sentence in sentences:
        words = sentence.split(" ")
        words_count.append(len(words))

    avg = sum(words_count)/len(sentences)
    return avg

def moreThanAvg(sentences, avg):
    longer_than_avg = []

    for sentence in sentences:
        words = sentence.split(" ")
        if len(words) > avg:
            longer_than_avg.append(sentence)

    return longer_than_avg

for s in sentences:
    print(s)

print(f"Priemerný počet slov vo vete je {avgWords(sentences)}")
print(f"Vety, dlhšie ako priemer sú: {moreThanAvg(sentences, avgWords(sentences))}")


