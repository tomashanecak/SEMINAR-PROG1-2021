import random

def linearSearch(array, searchin_for):
    print(array)
    for i, n in enumerate(array):
        if n == searchin_for:
            return f"Našiel sa hľadaný výraz -> {searchin_for} na indexe -> {i}"
    return f"Hľadaný výraz -> {searchin_for} sa nenašiel :("

print(linearSearch([random.randint(0,999) for x in range(1000)], 30))