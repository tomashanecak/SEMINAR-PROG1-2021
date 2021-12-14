n = int(input())

power = 1           
while power < 500:  
    if (power * n) > 500:
        print(power)
        break
    else:
        power = power * n

# n = int(input())
# power = 1
# while power * n < 500:
#     power = power * n
# print(power)