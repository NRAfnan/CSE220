import numpy as np


# You must run this cell to print matrix and for the driver code to work
def print_matrix(m):
    row, col = m.shape
    for i in range(row):
        c = 1
        print('|', end='')
        for j in range(col):
            c += 1
            if (len(str(m[i][j])) == 1):
                print(' ', m[i][j], end='  |')
                c += 6
            else:
                print(' ', m[i][j], end=' |')
                c += 6
        print()
        print('-' * (c - col))


def check_diagonal(matrix1, matrix2):
    matched = True
    first_arr_s_d = get_secondary_diagonal(matrix1)
    second_arr_p_d_r = get_primary_diagonal_reversed(matrix2)
    i = 0
    while i < len(first_arr_s_d):
        if first_arr_s_d[i] != second_arr_p_d_r[i]:
            matched = False
            break
        i += 1
    if matched:
        print("YES")
    else:
        print("NO")


def get_primary_diagonal_reversed(arr):
    row, col = arr.shape
    r = row - 1
    primary_diagonal = np.zeros(row)
    i = 0
    while r >= 0:
        primary_diagonal[i] = arr[r][r]
        i += 1
        r -= 1
    return primary_diagonal


def get_secondary_diagonal(arr):
    row, col = arr.shape
    r = 0
    secondary_diagonal = np.zeros(row)
    while r < row:
        secondary_diagonal[r] = arr[r][col - 1 - r]
        r += 1
    return secondary_diagonal

array1 = np.array([[0, 4, 1],
                   [7, 2, 5],
                   [3, 6, 0]])
array2 = np.array([[3, 6, 0],
                   [5, 2, 7],
                   [0, 4, 1]])

check_diagonal(array1, array2)  # This should print YES
print(".............")
array1 = np.array([[0, 9, 9, 1],
                   [9, 0, 2, 9],
                   [9, 3, 0, 9],
                   [4, 9, 9, 0]])
array2 = np.array([[4, 9, 9, 0],
                   [9, 0, 3, 9],
                   [9, 0, 2, 9],
                   [0, 9, 5, 1]])

check_diagonal(array1, array2)  # This should print NO
