import os
import math
path = os.path.dirname(__file__)

money = [100, 10, 1]

total_amount = 0
employees = []
payouts = []
with open(os.path.join(path, "mzdy.txt"), "r") as file:
    for line in file:
        line = line.strip()
        print(line)
        list_line = line.split(" ")
        total_amount += int(list_line[0])
        employees.append(list_line[1] + " " + list_line[2])
        payouts.append(int(list_line[0]))

print("----------------------------------------------")
print(f"Celková suma na vyplatenie = {total_amount}$")
print("----------------------------------------------")

def getNumOfMoneyForEmployee(payout):
    hundreds = math.trunc(payout/100)
    tens = math.trunc((payout-hundreds*100)/10)
    coins = ((payout-hundreds*100)-tens*10)

    return [hundreds, tens, coins]

total_mon = [0, 0, 0]
for i, payout in enumerate(payouts):
    mon = getNumOfMoneyForEmployee(payout)
    print(mon)
    total_mon = [a + b for a, b in zip(total_mon, mon)]
    print(f"Na vyplatenie zamestnanca {employees[i]} je  potrebných {mon[0]} x 100$, {mon[1]} x 10$ a {mon[2]} x 1$ mincí")

print("---------------------------------")
print(total_mon)

