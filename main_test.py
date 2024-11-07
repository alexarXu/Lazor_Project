from Board import Board
from Blocks import Blocks
from solver import solve_lazor_game
from read_bff import readf_bff
from compute_lazor_paths import compute_lazor_paths
import os
import time

def main():
    '''
    test all the .bff files in a given folder
    '''
    # obtain all .bff file in bff_files
    folder_path = "bff_files"
    bff_files = [f for f in os.listdir(folder_path) if f.endswith('.bff')]
    
    for bff_file in bff_files:
        print(f"\nTesting {bff_file}...")
        file_path = os.path.join(folder_path, bff_file)
        
        # read .bff file and initialize game_board
        original_board, A_num, B_num, C_num, lazor_position, lazor_direction, target = readf_bff(file_path)
        game_board = Board(original_board, A_num, B_num, C_num)
        game_board.push_target(target)
        
        start_time = time.time()

        solved_board = solve_lazor_game(game_board, A_num, B_num, C_num, lazor_position, lazor_direction, target)
        
        # record the time
        end_time = time.time()
        duration = end_time - start_time
        
        if solved_board:
            print(f"\n{bff_file} solved in {duration:.2f} seconds.")
            # solved_board.display_board()
        else:
            print(f"{bff_file} could not be solved within the given constraints. Took {duration:.2f} seconds.")
    
if __name__ == "__main__":
    main()