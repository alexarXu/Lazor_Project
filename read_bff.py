'''
This read_bff.py file is used to read the .bff file.

A .bff file includes the board, the number of blocks, and the lasers setting.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from utlis import check_if_the_point_in_grid

def readf_bff(file_path):
    '''
    This function to read the .bff file and return the board, the number of each blocks, 
    the laser setting (direction and postion) and the target points.
    
    ***Parameters***
    file_path: str, the path of the .bff file.
    ***Return***
    board: 2D list, the board of the game.
    A_num: int, the number of the reflect blocks.
    B_num: int, the number of the opaque blocks.
    C_num: int, the number of the refract blocks.
    lazor_position: 2D list, the position of the lazor.
    lazor_direction: 2D list, the direction of the lazor.
    target: 2D list, the target points.
    '''
    with(open(file_path)) as f:
        board = []
        original_board = []
        A_num = 0
        B_num = 0
        C_num = 0
        lazor_position = []
        lazor_direction = []
        target = []
        grid = []

        # read the content of the file and split it by lines
        bff = open(file_path, 'r').read().splitlines()

        # read the grid of the game, from "GRID START" to "GRID STOP"
        for i in range(len(bff)):
            if bff[i]=="GRID START":
                for j in range(i+1, len(bff)):
                    if bff[j]=="GRID STOP":
                        break
                    else:
                        board.append(bff[j])
        # read the number of each blocks
            elif len(bff[i]) == 3 and bff[i][0] == "A":
                A_num = int(bff[i][2])
            elif len(bff[i]) == 3 and bff[i][0]=="B":
                B_num = int(bff[i][2])
            elif len(bff[i]) == 3 and bff[i][0]=="C":
                C_num = int(bff[i][2])
        # read the lazor and target points
            elif len(bff[i]) != 0 and bff[i][0]=="L":
                lazor = bff[i].split(" ")
                if len(lazor) == 5:
                    lazor_position.append([int(lazor[1]), int(lazor[2])])
                    lazor_direction.append([int(lazor[3]), int(lazor[4])])
                else:
                    print("Invalid lazor setting! Please check the .bff file.")
        # read the target points
            elif len(bff[i]) != 0 and bff[i][0]=="P":
                target.append([int(bff[i][2]), int(bff[i][4])])
    # convert the board to the 2D list
    for x in board:
        lists = x.split()
        original_board.append(lists) 

    # convert the board to the grid, fulfill the empty space with 'x'
    # because the step is half of the block, so the size of the grid is 2*len+1
    n = len(original_board)
    m = len(original_board[0])
    grid = [['x' for _ in range(2 * m + 1)] for _ in range(2 * n + 1)]
    for i in range(n):
        for j in range(m):
            grid[2 * i + 1][2 * j + 1] = original_board[i][j]

    # check if the settings are valid 
    row = len(grid)
    column = len(grid[0])
    # check the laser settings
    if len(lazor) == 0:
        print('No laser! Please check the .bff file.')
    # check the laser position and direction
    for i in range(len(lazor_position)):
        if check_if_the_point_in_grid(lazor_position[i], grid) == False:
            print(f'Laser {i} starts out of the grid! Please check the .bff file.')
        if not (lazor_direction[i][0] in [-1, 1] and lazor_direction[i][1] in [-1, 1]):
            print(f'Invalid laser direction of laser {i}! Please check the .bff file.')

    # check the target points
    if len(target) == 0:
        print('No target point! Please check the .bff file.')
    for i in range(len(target)):
        if check_if_the_point_in_grid(target[i], grid) == False:
            print(f'Target point {i} is out of the grid! Please check the .bff file.')
    
    # check the block settings
    if (A_num + B_num + C_num) == 0:
        print('No usable blocks! Please check the .bff file.')
    if A_num < 0 or B_num < 0 or C_num < 0:
        print('Invalid block number! Please check the .bff file.')
    if (A_num + B_num + C_num) >= row * column:
        print('The number of blocks is greater than the grid size! Please check the .bff file.')

    # check the grid settings
    valid_chars = {'x', 'o', 'A', 'B', 'C'}
    for i in range(row):
        for j in range(column):
            if grid[i][j] not in valid_chars:
                print(f'Invalid character "{grid[i][j]}" at ({j}, {i}) in the grid!')

    return original_board, grid, A_num, B_num, C_num, lazor_position, lazor_direction, target


# if __name__ == "__main__":
    
#     data = readf_bff("C:/Users/administer/Desktop/SC/Lazor_Project/bff_files/mad_1.bff")
#     print(data)
