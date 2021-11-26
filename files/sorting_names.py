import os
path = os.path.dirname(__file__)


def SelectionSort(array):
    for i in range(len(array) - 1):
        n = array[i]
        ni = i

        # LINEAR SEARCH PART
        for j in range(i+1, len(array)):
            if array[j] < n:
                n = array[j]
                ni = j
        
        array[i], array[ni] = array[ni], array[i]
    return array

def main():
    what = int(input("Pre triedenie podľa mena zadaj 1, pre triedenie podľa dátumu narodenia zadaj 2 ->"))

    with open(os.path.join(path, "databaza02.txt"), "r") as file:

        if what == 1:
            names = []

            for row in file:
                row_list = row.split(" ")
                names.append(row_list[0])

            print(SelectionSort(names))

        elif what == 2:
            years = []

            for row in file:
                row_list = row.split(" ")
                date = row_list[-1].strip()
                years.append(date.split(".")[-1])
            
            print(SelectionSort(years))

        else:
            print("Zadaj číslo 1 alebo 2!!!")
            print("-------------------------")
            main()

main()
