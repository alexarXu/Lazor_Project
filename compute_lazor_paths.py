from Board import Board

def compute_lazor_paths(board):
    """
    Computes all possible lazor paths on the given board.
    
    Parameters:
        board (Board): An instance of the Board class with:
        - initial lazor positions and directions.
        - blocks map
        - target location.
        
    Returns:
        Board: Updated Board object with computed lazor paths stored in `board.all_lazor`.
    """
    
    lazor_position = board.lazor_position
    lazor_direction = board.lazor_direction

    # print('start')
    # Initialize lazor tracking queue with the initial lazor segments
    board.generate_initial_lazor()
    lazor_queue = board.initial_lazor
    # print(lazor_queue)

    max_steps = 100
    step_count = 0

    # Clear any existing lazor paths in `all_lazor` before computing
    board.all_lazor = []

    # Begin tracking the lazor path
    while lazor_queue and step_count < max_steps:
        current_lazor = lazor_queue.pop(0)  # Take the next lazor path to process
        step_count += 1

        # print(f"\nStep {step_count}: Current laser segment: {current_lazor}")

        try:
            # Determine the block the lazor will interact with
            interact_block = board.get_interact_block(current_lazor)
            if interact_block is None:
                # Lazor is out of bounds; store the path and continue
                board.all_lazor.append(current_lazor)
                # print(f"Lazor out of bounds at {current_lazor[2:]}.\n")
                continue  

            block_y, block_x = interact_block
            block = board.blocks_[block_y][block_x]
            # print(f"Laser interacts with block at ({block_y}, {block_x}), Block Type: {block.category}")

            # Execute lazor interaction and obtain resulting paths
            result_paths = block.lazor_interact(current_lazor)

            # Store current path in all_lazor for final tracking
            board.all_lazor.append(current_lazor)
            # print(f"Laser path added to history: {current_lazor}")

            # Add resulting paths to the queue for further processing
            for path in result_paths:
                if path is not None:
                    lazor_queue.append(path)  # Add each resulting path to the queue
                    # print(f"New laser path appended to queue: {path}")
                # else:
                #     print("Laser was blocked and did not continue.")
                    
        except ValueError as e:
            print(f"Error: {e}")
            break

    # print(f"\nTotal steps taken: {step_count}")
    return board  # Return the updated board with all lazor paths stored in `all_lazor`
