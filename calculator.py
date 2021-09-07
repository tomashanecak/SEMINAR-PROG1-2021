#Command to import data
number1 = int(input("Zadaj prvé číslo: "))
number2 = int(input("Zadaj druhé číslo: "))

# sum = number1 + number2
# mul = number1 * number2
# diff = number1 - number2
# div = number1 / number2

# print(number1, " + ", number2, " = ", sum)
# print(number1, " * ", number2, " = ", mul)
# print(number1, " - ", number2, " = ", diff)
# print(number1, " / ", number2, " = ", div)

operands = ["+","-","*","/"]

for i in range(4):
    operation = eval(f' {number1} {operands[i]} {number2}')
    print(number1, " ",operands[i]," ", number2, " = ", operation)







