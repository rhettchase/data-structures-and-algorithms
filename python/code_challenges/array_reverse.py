def reverseArray(arr):
    # calculate length of the original array
    length = len(arr)
    # initialize empty list to store the reversed elements (same length of the original array)
    reversed_arr = [0] * length

    # initialize index
    i = 0

    # iterate over the original array in reverse order and fill the new array

    while i < length:
        reversed_arr[i] = arr[length - 1 - i]
        i += 1

    return reversed_arr

print(reverseArray([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
