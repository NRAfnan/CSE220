# Task 4
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


def show_knight_move(knight):
    """
    1. We create the chess board of 0s
    2. The default num of knight moves is initialized
    3. Now for each move calculate the knights next pos from prev pos
    4. If the next pos is valid i.e. inside the chess board we update the board with 3
    :param knight: A tuple of position ex - (row, col)
    :return: A 2d array of 0s where the available moves are 3 and current position is 66
    """
    chess_board_of_0s = np.zeros((8, 8), dtype=int)
    chess_board_of_0s[knight[0]][knight[1]] = 66
    default_knight_moves = 8
    for i in range(default_knight_moves):
        starting_pos = np.array(knight)
        if i == 0:
            move_up_by_2(starting_pos)
            move_right(starting_pos)
            if 0 <= starting_pos[0] < 8 and 0 <= starting_pos[1] < 8:
                chess_board_of_0s[starting_pos[0]][starting_pos[1]] = 3
        elif i == 1:
            move_up_by_2(starting_pos)
            move_left(starting_pos)
            if 0 <= starting_pos[0] < 8 and 0 <= starting_pos[1] < 8:
                chess_board_of_0s[starting_pos[0]][starting_pos[1]] = 3
        elif i == 2:
            move_down_by_2(starting_pos)
            move_right(starting_pos)
            if 0 <= starting_pos[0] < 8 and 0 <= starting_pos[1] < 8:
                chess_board_of_0s[starting_pos[0]][starting_pos[1]] = 3
        elif i == 3:
            move_down_by_2(starting_pos)
            move_left(starting_pos)
            if 0 <= starting_pos[0] < 8 and 0 <= starting_pos[1] < 8:
                chess_board_of_0s[starting_pos[0]][starting_pos[1]] = 3
        elif i == 4:
            move_left_by_2(starting_pos)
            move_up(starting_pos)
            if 0 <= starting_pos[0] < 8 and 0 <= starting_pos[1] < 8:
                chess_board_of_0s[starting_pos[0]][starting_pos[1]] = 3
        elif i == 5:
            move_left_by_2(starting_pos)
            move_down(starting_pos)
            if 0 <= starting_pos[0] < 8 and 0 <= starting_pos[1] < 8:
                chess_board_of_0s[starting_pos[0]][starting_pos[1]] = 3
        elif i == 6:
            move_right_by_2(starting_pos)
            move_up(starting_pos)
            if 0 <= starting_pos[0] < 8 and 0 <= starting_pos[1] < 8:
                chess_board_of_0s[starting_pos[0]][starting_pos[1]] = 3
        elif i == 7:
            move_right_by_2(starting_pos)
            move_down(starting_pos)
            if 0 <= starting_pos[0] < 8 and 0 <= starting_pos[1] < 8:
                chess_board_of_0s[starting_pos[0]][starting_pos[1]] = 3
    return chess_board_of_0s


# because pos is an array the increment and decrement is happening in place
def move_left(pos):
    pos[1] -= 1


def move_right(pos):
    pos[1] += 1


def move_up(pos):
    pos[0] -= 1


def move_down(pos):
    pos[0] += 1


def move_left_by_2(pos):
    pos[1] -= 2


def move_right_by_2(pos):
    pos[1] += 2


def move_up_by_2(pos):
    pos[0] -= 2


def move_down_by_2(pos):
    pos[0] += 2


knight = (4, 3)
chess_board = show_knight_move(knight)
print_matrix(chess_board)
# This Should print
# | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
# ------------------------------------------
# | 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 |
# ------------------------------------------
# | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 |
# ------------------------------------------
# | 0 | 0 | 0 | 0 | 66 | 0 | 0 | 0 |
# ------------------------------------------
# | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 |
# ------------------------------------------
# | 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 |
# ------------------------------------------
# | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
# ------------------------------------------
# | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
# -----------------------------------------
