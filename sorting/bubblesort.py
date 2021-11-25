import random
import time
start_time = time.time()


def BubbleSort(array):
    sort = True
    while sort == True:
        sort = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i] , array[i+1] = array[i+1], array[i]
                sort = True
    return array

array = []
for i in range(1000000):
    array.append(random.randint(0,999))

print(array)
print(BubbleSort(array))
print("My program took", round(time.time() - start_time, 3), " seconds to run")