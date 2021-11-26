array = [12, 978, 0, 132, 16, 9999, 18768523]

def InsertionSort(array):
    for i in range(1, len(array)):
        j = 0
        while (j < i) and (array[j] < array[i]):
            j += 1
        sortedd = array[i]
        shift = array[j:i]
        array[j+1:i+1] = shift
        array[j] = sortedd
    return array

print(InsertionSort(array))