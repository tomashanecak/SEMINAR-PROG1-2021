import random

# def binarySearchRec(array, searching_for, length, left=0):
#     if left > length:
#         return f"Hľadaný výraz -> {searching_for} sa nenašiel :("
#     mid = left + int((length - left) / 2)

#     if   searching_for < array[mid]:
#         return binarySearch(array, searching_for, mid - 1, left)
#     elif searching_for > array[mid]:
#         return binarySearch(array, searching_for, length, mid + 1)
#     else:
#         return mid

# arr = [random.randint(1,50) for i in range(10)]
# arr.sort()
# print(arr)
# print(binarySearchRec(arr, 10, len(arr)-1))

def binarySearch(array, searching_for, length):
    left = 0
    right = length - 1

    while left <= right:
        mid = int((right+left) / 2)

        if array[mid] == searching_for:
            return f"Hľadaný prvok -> {searching_for} sa našiel na indexe -> {mid}"
        elif array[mid] < searching_for:
            left = mid + 1
        elif array[mid] > searching_for:
            right = mid - 1
    
    return f"Hľadaný prvok -> {searching_for} sa nenašiel"


arr = [random.randint(1,100) for i in range(10)]
arr.sort()
print(arr)
print(binarySearch(arr, 10, len(arr)))



