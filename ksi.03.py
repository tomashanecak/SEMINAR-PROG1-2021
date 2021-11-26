import math
# Vytvorte funkci na vypocet kvadraticke rovnice.
# Smazte prikaz `return None` a piste svuj program.
def solve(a: float, b: float, c: float) -> float:
    d = b**2-4*a*c

    if d < 0:
        return None
    else:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        
        if x1 > x2:
            return x1
        else:
            return x2
    

# priklady volani:
print(solve(2, -11, 14))  # 3.5
print(solve(1, 2, -63))  # 7.0
print(solve(1, 3, 7))  # None

# from math import sqrt


# def solve(a: float, b: float, c: float) -> float:
#     d: float = b**2 - 4*a*c
#     if d < 0:
#         return None

#     x1: float = (-b + sqrt(d)) / (2 * a)
#     x2: float = (-b - sqrt(d)) / (2 * a)
#     return max(x1, x2)
