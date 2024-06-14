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


def row_rotation(exam_week, seat_status):
    """
    1. From 1 to exam_week(excluded), each week we will rotate
    2. Next, we will print modified exam seat status
    :param exam_week: an int but  in this case the start will not start from 0 but rather from 1
    :param seat_status: a numpy 2d array of seat status
    :return: The position of our friend "AA"
    """
    for i in range(1, exam_week):
        rotate_columns(seat_status)
    print(seat_status)
    # Let us think that our friend always starts their week 1 at last row
    # so after shifting (row + (exam_week - 1)) % row
    row = len(seat_status)
    friend_row = (row + (exam_week - 1)) % row
    if friend_row == 0:
        friend_row = row
    return friend_row

def rotate_columns(arr):
    """
    We need to right rotate or downwards rotation in this case
    1. Hold the value of the last row
    2. Iterate column wise
    3. Iterate each row
    4. Right shift all the elements one by one from each row in the column
    5. Replace the first value with the last value
    :param arr: numpy 2d array
    :return: once rotated numpy 2d array
    """
    row, col = arr.shape
    c = 0
    while c < col:
        r = row - 1
        last_elem = arr[r][c]
        while r > 0:
            arr[r][c] = arr[r - 1][c]
            r -= 1
        arr[0][c] = last_elem
        c += 1


seat_status = np.array([['A', 'B', 'C', 'D', 'E'],
                        ['F', 'G', 'H', 'I', 'J'],
                        ['K', 'L', 'M', 'N', 'O'],
                        ['P', 'Q', 'R', 'S', 'T'],
                        ['U', 'V', 'W', 'X', 'Y'],
                        ['Z', 'AA', 'BB', 'CC', 'DD']])
exam_week = 3
print_matrix(seat_status)
print()
row_number = row_rotation(exam_week, seat_status)  # This should print modified seat status after rotation
print(f'Your friend AA will be on row {row_number}')  # This should print Your friend AA will be on row 2
