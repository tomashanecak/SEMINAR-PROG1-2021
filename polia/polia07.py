## Vstupuje zadaný počeet viet, A) Zotriedťe slová vo vete podľa abecedy, zotrieďte písmenká v slove podľa abecedy

num_sent = int(input("Zadajte počet viet ako celé číslo: "))

sentences = []

for i in range(num_sent):
    sentences.append(str(input(f"Zadaj vetu č.{i+1}: ")))

def sortWords(sentence):
    words = sentence.split(" ")
    words.sort()
    return " ".join(words)

def sortCharacters(sentence):
    words = sentence.split(" ")
    words.sort()
    for w in words:
        chars = list(w)
        chars.sort()
    return eor

for i in range(len(sentences)):
    print(sortWords(sentences[i]))
    print(sortCharacters(sentences[i]))

