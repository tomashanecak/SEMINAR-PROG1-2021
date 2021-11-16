import random as r
rows = int(input("Zadaj počet riadkov: "))
cols = int(input("Zadaj počet stĺpcov: "))

matrix = []
row = []

for i in range(rows):
    if len(row) > 0: matrix.append(row)
    row = []
    for j in range(cols):
        row.append(r.randint(10,999))

def printMatrix():
    for row in matrix:
        row_sum = sum(row)
        print(row, end=" Súčet = ")
        print(row_sum)

print("-------------------------------------")
printMatrix()
print("-------------------------------------")

for i in range(len(matrix) - 1):
    for j in range(len(matrix) - 1):
        if sum(matrix[j]) > sum(matrix[j+1]):
            matrix[j], matrix[j+1] = matrix[j+1], matrix[j]

printMatrix()



