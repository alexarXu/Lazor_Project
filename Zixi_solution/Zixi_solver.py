
from itertools import combinations
from .Board import Board
from .compute_lazor_paths import compute_lazor_paths
from .read_bff import readf_bff

def solve_lazor_game(board):
    """
    Solve the lazor game by testing all possible block arrangements.

    Parameters:
        board (Board): The initial board layout, including block numbers, lazor sources, directions, and targets.

    Returns:
        Board: Solved board configuration, or None if no solution is found.
    """
    empty_positions = [(x, y) for x in range(board.width) for y in range(board.height) if board.original_board[y][x] == 'o']
    
    #testing all possible block arrangement
    for a_positions in combinations(empty_positions, board.A_num):
        for b_positions in combinations([p for p in empty_positions if p not in a_positions], board.B_num):
            for c_positions in combinations([p for p in empty_positions if p not in a_positions + b_positions], board.C_num):
                
                board.clear_blocks()

                for pos in a_positions:
                    board.place_blocks(pos, 'A')
                for pos in b_positions:
                    board.place_blocks(pos, 'B')
                for pos in c_positions:
                    board.place_blocks(pos, 'C')

                board = compute_lazor_paths(board)

                if board.check_targets_reached():
                    print("Solution found")
                    return board  

    print("No solution found.")
    return None  
