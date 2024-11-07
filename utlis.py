import numpy as np
import pandas as pd

def find_occupied_spots(small_grid):
    positions = []
    for i in range(len(small_grid)):
        for j in range(len(small_grid[0])):
            block = small_grid[i][j]
            if block in ['A', 'B', 'C']:
                positions.append([i * 2 + 1, j * 2 + 1])
    return positions


def obvious_skip(grid, possibles, lst, holes):
    for i in range(len(holes)):
        x = holes[i][1]
        y = holes[i][0]
        if ((grid[x][y + 1] in ['A', 'B']) and (grid[x][y - 1] in ['A', 'B'])) or \
                ((grid[x + 1][y] in ['A', 'B']) and (grid[x - 1][y] in ['A', 'B'])):
            return False
        else:
            return True
        
def check_if_the_point_in_grid(point, grid):
    column = len(grid[0])
    row = len(grid)
    if not (0 <= point[0] <= column * 2 and 0 <= point[1] <= row * 2):
        return False