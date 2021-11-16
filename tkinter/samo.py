import random
pole = []
pole2 = []

for i in range(10):
    pole.append(pole2)
    pole2 = []
    for j in range(3):
        pole2.append(random.randint(1,10))

for p in pole:
    print(p)

print(pole[3][1])

