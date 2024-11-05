from itertools import product
from copy import deepcopy
from Board import Board

def solve_lazor_game(board):
    """
    Solves the lazor game by finding a combination of blocks that
    allows all targets to be hit by lazor paths.

    Parameters:
        board (Board): An instance of the Board class with:
        - initial lazor positions and directions.
        - blocks map
        - target location.
    
    Returns:
        Board: Updated Board object with the solution, or None if no solution found.
    """

    # 找到所有空位置，即可以放置块的位置
    empty_positions = [
        (x, y) for y in range(board.height) for x in range(board.width)
        if board.original_board[y][x] == 'o'
    ]

    # 获取所有可能的块类型排列组合
    possible_blocks = ['A'] * board.A_num + ['B'] * board.B_num + ['C'] * board.C_num + ['O'] * len(empty_positions)

    # 尝试所有排列组合
    for block_combination in product(possible_blocks, repeat=len(empty_positions)):
        # 只尝试有效的组合，跳过冗余的组合
        if block_combination.count('A') == board.A_num and \
           block_combination.count('B') == board.B_num and \
           block_combination.count('C') == board.C_num:

            # 重置棋盘
            board.clear_blocks()

            # 在棋盘上放置当前组合的块
            for position, block_type in zip(empty_positions, block_combination):
                if block_type != 'O':  # 只放置非空块
                    board.place_blocks(position, block_type)

            # 计算激光路径
            compute_lazor_paths(board)

            # 检查是否所有目标都被击中
            if board.check_targets_reached():
                print("Solution found!")
                return board  # 找到解返回

    print("No solution found.")
    return None  # 如果没有解，则返回 None
