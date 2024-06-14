# Task 6
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


def play_game(arena):
    """
    1. We iterate for each item in the arena 2d array
    2. If we get a multiple of 50 in (r, c)th position
    3. We check for 2s in (r, c - 1), (r - 1, c), (r, c + 1), (r + 1, c) if the positions are valid (meaning inside the arena)
    4. We add them and check if they are inside the range of survival
    :param arena:
    :return:
    """
    survival_points = 10
    get_points_from = np.array([[0, -1], [-1, 0], [0, 1], [1, 0]])
    team_points = 0
    row, col = arena.shape
    r = 0
    while r < row:
        c = 0
        while c < col:
            if arena[r][c] % 50 == 0 and arena[r][c] != 0:
                player_pos = np.array([r, c])
                for pos in get_points_from:
                    points_pos = player_pos + pos
                    if (0 <= points_pos[0] < row) and (0 <= points_pos[1] < col) and (arena[points_pos[0]][points_pos[1]] == 2):
                        team_points += arena[points_pos[0]][points_pos[1]]
            c += 1
        r += 1
    if team_points >= survival_points:
        print(f"Points Gained: {team_points}. Your team has survived the game.")
    else:
        print(f"Points Gained: {team_points}. Your team is out.")

arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 6. Your team is out.

print(".....................")
arena=np.array([[0,2,2,0,2],
                [1,50,2,1,100],
                [2,2,2,0,2],
                [0,200,2,0,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 14. Your team has survived the game.