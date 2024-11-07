import numpy as np
import pandas as pd

def find_block_positions(grid):
    '''
    This function finds the positions of the blocks in the grid.
    ***Parameters***
    grid: 2D list, the grid of the game.
    ***Returns***
    block_positions: list, the positions of the blocks in the grid.
    '''
    block_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            block = grid[i][j]
            if block in ['A', 'B', 'C','D']:
                block_positions.append([i * 2 + 1, j * 2 + 1])
    return block_positions


def faster_trick_skip(grid, possibles, lst, target_points):
    '''
    This function checks if the grid can be skipped.
    Found that if the target points are surrounded by two blocks, the grid can be skipped.
    like:
    x x x x x
    x A · A x
    x x x x x
    In this case, the grid can be skipped.
    ***Parameters***
    grid: 2D list, the grid of the game.
    possibles: list, the possible permutations of the blocks.
    lst: list, the current permutation of the blocks.
    target_points: list, the positions of the target points.
    ***Returns***
    give a binary choice of whether the grid can be skipped
    True if the grid can be skipped, False otherwise.
    '''
    for i in range(len(target_points)):
        x = target_points[i][1]
        y = target_points[i][0]
        if ((grid[x][y + 1] in ['A', 'B', 'C', 'D']) and (grid[x][y - 1] in ['A', 'B', 'C', 'D'])) or \
                ((grid[x + 1][y] in ['A', 'B', 'C', 'D']) and (grid[x - 1][y] in ['A', 'B', 'C', 'D'])):
            return False
        else:
            return True
        
def check_if_the_point_in_grid(point, grid):
    '''
    This function checks if the point is in the grid.
    ***Parameters***
    point: list, the point to be checked.
    grid: 2D list, the grid of the game.
    ***Returns***
    True if the point is in the grid, False otherwise.
    '''
    column = len(grid[0])
    row = len(grid)
    if not (0 <= point[0] <= column * 2 and 0 <= point[1] <= row * 2):
        return False