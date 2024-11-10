from Beiya_solution.board_solver import beiya_solver

from Zixi_solution.Zixi_solver import solve_lazor_game
from Zixi_solution.read_bff import readf_bff

import os
import time

def main():
    '''
    Test all the .bff files in a given folder.
    '''
    # Obtain all .bff files in the bff_files folder
    folder_path = "bff_files"
    bff_files = [f for f in os.listdir(folder_path) if f.endswith('.bff')]
    
    for bff_file in bff_files:
        print(f"\nTesting {bff_file}...")

        file_path = os.path.join(folder_path, bff_file)
        print('Beiya Solution:')
        start_time = time.time()
        # Solve the puzzle
        updated_grid, solution, lazor_path = beiya_solver(file_path)
        end_time = time.time()
        duration = end_time - start_time
        if solution != 0:
            print(f"\n{bff_file} solved in {duration:.2f} seconds.")
        else:
            print(f"{bff_file} could not be solved. Took {duration:.2f} seconds.")

        print('Zixi Solution:')
        start_time = time.time()
        # Read the .bff file and initialize the game board
        game_board = readf_bff(file_path)
        # Solve the lazor game
        solved_board_zixi = solve_lazor_game(game_board)
        # Record the time taken
        end_time = time.time()
        duration = end_time - start_time
        # Output results
        if solved_board_zixi:
            print(f"\n{bff_file} solved in {duration:.2f} seconds.")
            solved_board_zixi.display_board()
        else:
            print(f"{bff_file} could not be solved. Took {duration:.2f} seconds.")
    
if __name__ == "__main__":
    main()
