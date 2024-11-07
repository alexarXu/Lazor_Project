
from Board import Board
from solver import solve_lazor_game
from read_bff import readf_bff
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
        
        # Read the .bff file and initialize the game board
        game_board = readf_bff(file_path)
        
        start_time = time.time()

        # Solve the lazor game
        solved_board = solve_lazor_game(game_board)
        
        # Record the time taken
        end_time = time.time()
        duration = end_time - start_time
        
        # Output results
        if solved_board:
            print(f"\n{bff_file} solved in {duration:.2f} seconds.")
            solved_board.display_board()
        else:
            print(f"{bff_file} could not be solved. Took {duration:.2f} seconds.")
    
if __name__ == "__main__":
    main()
