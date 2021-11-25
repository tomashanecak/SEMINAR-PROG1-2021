import random
import time
bubble_sort_time = 0
selection_sort_time = 0
insertion_sort_time = 0

array = []
for i in range(10):
    array.append(random.randint(0,999))

array1 = array2 = array

def BubbleSort(array):
    bubble_sort_start_time = time.time()
    sort = True
    while sort == True:
        sort = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i] , array[i+1] = array[i+1], array[i]
                sort = True
    
    bubble_sort_time = time.time()
    print("My program took", bubble_sort_time - bubble_sort_start_time, " seconds to run")
    return array

def SelectionSort(array):
    selection_sort_start_time = time.time()
    for i in range(len(array) - 1):
        n = array[i]
        ni = i

        # LINEAR SEARCH PART
        for j in range(i+1, len(array)):
            if array[j] < n:
                n = array[j]
                ni = j
        
        array[i], array[ni] = array[ni], array[i]

    selection_sort_time = time.time()
    print("My program took", selection_sort_time - selection_sort_start_time, " seconds to run")
    return array

def InsertionSort(array):
    insertion_sort_start_time = time.time()
    for i in range(1, len(array)):
        j = 0
        while (j < i) and (array[j] < array[i]):
            j += 1
        small = array[i]
        shift = array[j:i]
        array[j+1:i+1] = shift
        array[j] = small

    insertion_sort_time = time.time()
    print("My program took", insertion_sort_time - insertion_sort_start_time, " seconds to run")
    return array
    

print(array)

print("Bubble Sort")
print(BubbleSort(array))

print("Selection Sort")
print(SelectionSort(array1))

print("Insertion Sort")
print(InsertionSort(array2))

