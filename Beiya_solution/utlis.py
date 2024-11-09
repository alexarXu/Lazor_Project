import numpy as np
import pandas as pd

def find_block_positions(board):
    '''
    This function finds the positions of the blocks in the grid.
    ***Parameters***
    grid: 2D list, the grid of the game.
    ***Returns***
    block_positions: list, the positions of the blocks in the grid.
    '''
    block_positions = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            block = board[i][j]
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
        if ((grid[x][y + 1] in ['A', 'B']) and (grid[x][y - 1] in ['A', 'B'])) or \
                ((grid[x + 1][y] in ['A', 'B']) and (grid[x - 1][y] in ['A', 'B'])):
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


def multiset_permutations_subs(iterable):
    '''
    This function generates the multiset permutations of the iterable.
    It is the same as sympy.utilities.iterables.multiset_permutations but without the sympy dependency.
    It can also be used to generate the permutations of the elements in the list.
    ***Parameters***
    iterable: list, the list to be permuted.
    ***Returns***
    The multiset permutations of the iterable.
    '''
    def permute_unique(elements):
        if len(elements) <= 1:
            yield elements
        else:
            unique_elements = set(elements)
            for first_element in unique_elements:
                remaining_elements = list(elements)
                remaining_elements.remove(first_element)
                for sub_permutation in permute_unique(remaining_elements):
                    yield [first_element] + sub_permutation

    return permute_unique(sorted(iterable))
