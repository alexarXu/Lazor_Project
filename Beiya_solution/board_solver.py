import copy
import time 
from PIL import ImageDraw, Image
from sympy.utilities.iterables import multiset_permutations

from read_bff import readf_bff
from define_grid import Grid
from define_lazor import Lazor
from utlis import *
from board_visualization import image_output

def path_seek(grid, num_blocks_of_type_a, num_blocks_of_type_b, num_blocks_of_type_c, lazor_list, hole_list, position):
    blocks = []
    # Extract the blank positions and replace them with blocks
    for row in grid:
        for element in row:
            if element == 'o':
                blocks.append(element)
    for i in range(num_blocks_of_type_a):
        blocks[i] = 'A'
    for i in range(num_blocks_of_type_a, (num_blocks_of_type_a + num_blocks_of_type_b)):
        blocks[i] = 'B'
    for i in range((num_blocks_of_type_a + num_blocks_of_type_b),
                   (num_blocks_of_type_a + num_blocks_of_type_b + num_blocks_of_type_c)):
        blocks[i] = 'C'
    # Generate a list of permutations of blocks and blank positions
    block_permutations = list(multiset_permutations(blocks))

    while len(block_permutations) != 0:
        blocks_temp = block_permutations[-1]
        blocks_temp_save = copy.deepcopy(blocks_temp)
        block_permutations.pop()
        # Generate a board from the grid function
        print(grid)
        original_grid = Grid(grid)
        test_board = original_grid.generate_grid(blocks_temp, position)
        # print(position)
        # print(test_board)
        # Test the board with the obvious_skip function and run it through Lazor to see if it is the right board
        if faster_trick_skip(test_board, block_permutations, blocks_temp, hole_list):
            lazor = Lazor(test_board, lazor_list, hole_list)
            solution = lazor.lazor_path()
            # Return 0 if the board is wrong and return a list with the path of lazor if it's right
            if solution != 0:
                return solution, blocks_temp_save, test_board
            else:
                continue


def solver(fptr):
    data = readf_bff(fptr)
    grid = data[0]
    num_cols = data[1]
    num_rows = data[2]
    num_holes = data[3]
    lazors = data[4]
    holes = data[5]
    small_grid = data[6]
    print(data)
    # Find the positions of the occupied spots in the grid
    occupied_spots = find_block_positions(small_grid)
    print(occupied_spots)
    # Solve the puzzle and find the path of the lazors
    solution, lazor_path = path_seek(grid, num_cols, num_rows, num_holes, lazors, holes, occupied_spots)[:2]

    # Create a new grid with the lazors and holes
    new_grid = copy.deepcopy(small_grid)
    lazor_index = 0
    for row in range(len(new_grid)):
        for col in range(len(new_grid[0])):
            if new_grid[row][col] == 'o':
                new_grid[row][col] = lazor_path[lazor_index]
                lazor_index += 1

    # Generate output image
    image_output(solved_board=new_grid, answer_lazor=solution, lazor_info=lazors,
                 holes=holes, filename=fptr)
    output_filename = '.'.join(fptr.split('.')[0:-1])
    print('The puzzle has been solved and saved as {}'.format(
        output_filename + '_solved.png'))
    return new_grid, solution, lazor_path

