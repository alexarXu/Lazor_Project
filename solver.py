from itertools import combinations
from Board import Board
from compute_lazor_paths import compute_lazor_paths
from read_bff import readf_bff
import time

def solve_lazor_game(board, A_num, B_num, C_num, lazor_position, lazor_direction, target):
    """
    Solve the lazor game by testing all possible block arrangements.

    Parameters:
        board (Board): The initial board layout.
        A_num (int): Number of reflective blocks available.
        B_num (int): Number of opaque blocks available.
        C_num (int): Number of refractive blocks available.
        lazor_position (list): Initial lazor source positions.
        lazor_direction (list): Initial lazor directions.
        target (list): Target points on the board.

    Returns:
        Board: Solved board configuration, or None if no solution is found.
    """

    start_time = time.time()
    # 找出可以放置块的位置
    empty_positions = [(x, y) for x in range(board.width) for y in range(board.height) if board.original_board[y][x] == 'o']
    
    # 遍历可能的块组合
    for a_positions in combinations(empty_positions, A_num):
        for b_positions in combinations([p for p in empty_positions if p not in a_positions], B_num):
            for c_positions in combinations([p for p in empty_positions if p not in a_positions + b_positions], C_num):
                
                # 重置棋盘
                board.clear_blocks()

                # 放置 A、B 和 C 块
                for pos in a_positions:
                    board.place_blocks(pos, 'A')
                for pos in b_positions:
                    board.place_blocks(pos, 'B')
                for pos in c_positions:
                    board.place_blocks(pos, 'C')

                # 计算激光路径
                board = compute_lazor_paths(board)

                # 检查是否所有目标被击中
                if board.check_targets_reached():
                    end_time = time.time()
                    print(f"Solution found in {end_time - start_time:.2f} seconds!")
                    return board  # 返回解决方案

    end_time = time.time()
    print(f"No solution found. Execution time: {end_time - start_time:.2f} seconds.")
    return None  # 如果没有找到解决方案

