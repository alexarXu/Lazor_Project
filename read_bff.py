'''
This read_bff.py file is used to read the .bff file.

A .bff file includes the board, the number of blocks, and the lasers setting.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

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
                lazor_position.append([int(lazor[1]), int(lazor[2])])
                lazor_direction.append([int(lazor[3]), int(lazor[4])])
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

    # check if the grid is valid
    valid_blocks = {'x', 'o', 'A', 'B', 'C'}
    for i, row in enumerate(original_board):
        for j, char in enumerate(row):
            if char not in valid_blocks:
                raise Exception(f'Invalid character "{char}" at ({j}, {i}) in the grid!')
            
    # check if the blocks are valid - category A, B, C & nums
    if A_num==0 and B_num==0 and C_num == 0:
        print("There is no usable blocks! Please check the .bff file.")
    if A_num < 0 or B_num < 0 or C_num < 0:
        print("Invalid block number! Please check the .bff file.")
    if A_num + B_num + C_num > n * m:
        print("The number of blocks is greater than the grid size! Please check the .bff file.")

    # check if the lasers are valid
    if lazor == 0:
        print("There is no lazor! Please check the .bff file.")
    for i in range(len(lazor)):
        if lazor[i] !=4:
            print("Invalid lazor setting! Please check the .bff file.")
    for i in range(len(lazor_position)):
        if not (lazor_position[i][0] in [0, 2 * n] and lazor_position[i][1] in [0, 2 * m]):
            print("Invalid lazor position! Please check the .bff file.")
        if not (lazor_direction[i][0] in [-1, 1] and lazor_direction[i][1] in [-1, 1]):
            print("Invalid lazor direction! Please check the .bff file.")

    # check if the target points are valid
    if target == 0:
        print("There is no target point! Please check the .bff file.")
    for i in range(len(target)):
        if not (target[i][0] in [0, 2 * n] and target[i][1] in [0, 2 * m]):
            print("Invalid target point! Please check the .bff file.")

    return original_board, grid, A_num, B_num, C_num, lazor_position, lazor_direction, target


# if __name__ == "__main__":
#     time1 = time.time()
#     original_board, grid, A_num, B_num, C_num, lazor_position, lazor_direction, target = readf_bff("C:/Users/administer/Desktop/SC/lazor/Lazors-Project/mad_1.bff")
#     print(original_board)
#     print(grid)
#     print(A_num)
#     print(B_num)
#     print(C_num)
#     print(lazor_position)
#     print(lazor_direction)
#     print(target)
#     time2 = time.time()
#     print("The time used is: ", time2-time1)