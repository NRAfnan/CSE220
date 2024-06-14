# Task 5
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


def compress_matrix(mat):
    """
    1. We create the compressed array
    2. We iterate the given matrix with an increment of 2
    3. Add the (i, j), (i + 1, j), (i, j + 1) and (i + 1, j + 1) and put it inside the compressed array
    :param mat: A matrix with even row and columns
    :return: Compressed matrix
    """
    row, col = mat.shape
    row_c, col_c = row // 2, col // 2
    compressed_arr = np.zeros((row_c, col_c), dtype=int)
    r = 0
    r_c = 0
    while r < row:
        c = 0
        c_c = 0
        while c < col:
            compressed_arr[r_c][c_c] = (mat[r][c]) + (mat[r + 1][c]) + (mat[r][c + 1]) + (mat[r + 1][c + 1])
            c_c += 1
            c += 2
        r += 2
        r_c += 1
    return compressed_arr


def compress_matrix(mat):
    """
    Compress the given matrix by summing 2x2 blocks of elements.

    1. We create the compressed array
    2. We iterate the given matrix with an increment of 2
    3. Add the (i, j), (i + 1, j), (i, j + 1), and (i + 1, j + 1) and put it inside the compressed array

    :param mat: A matrix with even rows and columns
    :return: Compressed matrix
    """
    # Get the dimensions of the original matrix
    row, col = mat.shape
    # Calculate the dimensions of the compressed matrix
    row_c, col_c = row // 2, col // 2
    # Initialize the compressed array with zeros
    compressed_arr = np.zeros((row_c, col_c), dtype=int)

    # Initialize row and row index for the compressed matrix
    r = 0
    r_c = 0

    # Iterate over rows of the original matrix with an increment of 2
    while r < row:
        # Initialize column and column index for the compressed matrix
        c = 0
        c_c = 0

        # Iterate over columns of the original matrix with an increment of 2
        while c < col:
            # Sum the 2x2 block of elements and put it in the compressed array
            compressed_arr[r_c][c_c] = (mat[r][c]) + (mat[r + 1][c]) + (mat[r][c + 1]) + (mat[r + 1][c + 1])

            # Move to the next column in the compressed array
            c_c += 1
            # Move to the next column in the original matrix with an increment of 2
            c += 2

        # Move to the next row in the compressed array
        r_c += 1
        # Move to the next row in the original matrix with an increment of 2
        r += 2

    # Return the compressed array
    return compressed_arr


matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
returned_array = compress_matrix(matrix)
print_matrix(returned_array)
#This should print
#|  14  |  22 |
#--------------
#|  2  |  10  |
#--------------