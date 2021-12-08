"""
V textovom súbore vek_muzov_zien.txt sú uložené údaje veku mužov a žien tak, že prvý riadok obsahuje dve čísla oddelené medzerou vyjadrujúce počet mužov a žien. Na každom nasledujúcom riadku je údaj veku a mena osoby. Údaje veku žien sú v súbore zapísané až po údajoch veku mužov.
Príklad zápisu v súbore:
3 2
42 Kavka Peter
21 Zaujec Vladimir
19 Adamica Matej
25 Urbanova Daniela
33 Abrahamova Iveta
Vytvorte program, ktorý:
- načíta údaje mužov a žien do prvkov dvoch jednorozmerných polí,
- polia s údajmi vypíše samostatne pre mužov a ženy zotriedené podľa abecedy a pod nimi na novom riadku vypíšte priemerný vek podľa pohlavia.

"""
import os 

path = os.path.dirname(__file__)

file = "vek_muzov_zien.txt"

with open(os.path.join(path+"\\"+file), "r") as file:
    men_count = int(list(str(file.readline()))[0])
    
    men = []
    women = []

    for i, filerow in enumerate(file):
        if i < men_count:
            men.append(filerow)
        else:
            women.append(filerow)


def BubbleSort(arr):
    sort = True

    while sort == True:
        sort = False
        
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                sort = True
    return arr

def sortNames(array):
    list_names = []
    for element in array:
        name = element.split(" ")[1]
        list_names.append(name)

    return BubbleSort(list_names)

def printSortedDB(gender):
    sorted_names = sortNames(gender)
    for x in sorted_names:
        for y in gender:
            if x in y:
                print(y)

def printGenderAvarage(gender):
    count = 0
    for i in range(len(gender)):
        count += int(gender[i].split(" ")[0])

    print(count/len(gender))


printSortedDB(men)
printGenderAvarage(men)

printSortedDB(women)
printGenderAvarage(women)





    



    

    

