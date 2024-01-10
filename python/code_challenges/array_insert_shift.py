import math

def insertShiftArray(arr, int):
    halfway_i = math.ceil(len(arr)/2)

    arr.append(None) # add placeholder at the end of the list to make room for new element

    # iterates in reverse order to the halfway pt index
    # each element at index i is replaced with the element at the previous index, which shifts the elements one position to the right
    for i in range(len(arr) - 1, halfway_i, -1):
        arr[i] = arr[i - 1]

    arr[halfway_i] = int

    return arr

print(insertShiftArray([42,8,15,23,42], 16))
# [42, 8, 15, 23, 42]
# [42, 8, 15, 23, 42, 42]
# [42, 8, 15, 23, 23, 42]
# [42, 8, 15, 16, 23, 42]
