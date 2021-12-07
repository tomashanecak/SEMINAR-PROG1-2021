import os
filename = "db.txt"

db_arr = []

##bywhat == 1 -> age; bywhat == 0 -> name
def BubbleSort(arr, bywhat):
    sort = True
    while sort == True:
        sort = False
        for i in range(len(arr) - 1):
            if arr[i].split(" ")[bywhat] > arr[i+1].split(" ")[bywhat]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sort = True
    return arr

def BinarySearch(arr, what, arr_len):
    left = 0
    right = arr_len - 1
    
    while left<= right:
        mid = int((right+left)/2)

        if arr[mid].split(" ")[0] == what:
            year = arr[mid].split(" ")[1]
            return f"{what} sa nasiel v databaze a jeho rok narodenia je {year}"
        elif arr[mid].split(" ")[0] < what:
            left = mid + 1
        elif arr[mid].split(" ")[0] > what:
            right = mid - 1
            
    return f"{what} sa v databaze nenasiel"


with open(filename, "r") as file:
    for row in file:
        db_arr.append(row.strip())

    print("Origo: ", db_arr)
    db_arr = BubbleSort(db_arr, 1)
    print("Zoradene: ", db_arr)
    print("Najstarsi: ", db_arr[:3])
    print("Najmladsi: ", db_arr[-3:])


    db_arr = BubbleSort(db_arr, 0)
    print(db_arr)
    name = str(input("Zadaj meno vyhladavanej osoby: "))
    print(BinarySearch(db_arr, name, len(db_arr)))





