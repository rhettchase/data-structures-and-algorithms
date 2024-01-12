my_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def matrix_sum(matrix):
    sum_list = []

    for row in matrix:
        sum = 0
        for item in row:
            sum += item
        sum_list.append(sum)

    return sum_list

print(matrix_sum(my_matrix))




