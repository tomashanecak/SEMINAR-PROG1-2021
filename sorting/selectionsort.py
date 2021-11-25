array = [12, 978, 0, 132, 16, 9999, 18768523]

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

print(SelectionSort(array))

        

