'''
This read_bff.py file is used to read the .bff file.

A .bff file includes the board, the number of blocks, and the lasers setting.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

        bff = open(file_path, 'r').read().splitlines()

        for i in range(len(bff)):
            if bff[i]=="GRID START":
                for j in range(i+1, len(bff)):
                    if bff[j]=="GRID STOP":
                        break
                    else:
                        board.append(bff[j])
            elif len(bff[i]) == 3 and bff[i][0] == "A":
                A_num = int(bff[i][2])
            elif len(bff[i]) == 3 and bff[i][0]=="B":
                B_num = int(bff[i][2])
            elif len(bff[i]) == 3 and bff[i][0]=="C":
                C_num = int(bff[i][2])
            elif len(bff[i]) != 0 and bff[i][0]=="L":
                lazor = bff[i].split(" ")
                lazor_position.append([int(lazor[1]), int(lazor[2])])
                lazor_direction.append([int(lazor[3]), int(lazor[4])])
            elif len(bff[i]) != 0 and bff[i][0]=="P":
                target.append([int(bff[i][2]), int(bff[i][4])])

    for x in board:
        lists = x.split()
        original_board.append(lists)
 
    return original_board, A_num, B_num, C_num, lazor_position, lazor_direction, target

def convert_to_grid(borad):
    '''
    This function is used to convert the board to the grid.
    
    ***Parameters***
    board: 2D list, the board of the game.
    permut: list, the permutation of the blocks.
    ***Return***
    grid: 2D list, the grid of the game
    '''
    n = len(board)
    m = len(board[0])
    
    # 创建一个 (2n + 1) x (2m + 1) 的网格，初始化为 'x'
    grid = [['1' for _ in range(2 * m + 1)] for _ in range(2 * n + 1)]
    
    for i in range(n):
        for j in range(m):
            # 将棋盘元素放置在网格的适当位置
            grid[2 * i + 1][2 * j + 1] = board[i][j]
    
    return grid

if __name__ == "__main__":
    board, A_num, B_num, C_num, lazor_position, lazor_direction, target = readf_bff("C:/Users/administer/Desktop/SC/Lazor_Project/bff_files/dark_1.bff")
    print(board)
    print(A_num)
    print(B_num)
    print(C_num)
    print(lazor_position)
    print(lazor_direction)
    print(target)
    grid = convert_to_grid(board)
    for row in grid:
        print(' '.join(row))