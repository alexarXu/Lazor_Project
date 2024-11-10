
from .Blocks import Blocks
import copy

class Board:
    '''
    Store the board as a class.
    Lazors are stored in single units in the format of (x0, y0, x1, y1).
    
    There are two coordinate systems:
    1- m*n to store blocks
    2- (2m-1) *(2n-1) to store lazor and target

    Blocks are stored in the attribute self.blocks_ as instances of the `Blocks` class.
    '''

    def __init__(self, original_board, A_num, B_num, C_num, lazor_position, lazor_direction, target):
        self.original_board = original_board
        self.height = len(self.original_board) 
        self.width = len(self.original_board[0])
        
        # Initialize blocks and lazor-related attributes
        self.original_blocks = self.add_original_blocks()
        self.blocks_ = copy.deepcopy(self.original_blocks)

        self.all_lazor = []  # Stores all lazor paths
        self.initial_lazor = []  # Initial lazor segments

        # Assign lazor positions, directions, and targets directly from parameters
        self.lazor_position = lazor_position
        self.lazor_direction = lazor_direction
        self.target = target

        # Number of each block type
        self.A_num, self.B_num, self.C_num = A_num, B_num, C_num

        # Generate the initial lazor path
        self.generate_initial_lazor()\
    
    def vtc_or_hrz(self, lazor):
        '''
        Identify the side from which the lazor approaches:
            - 'vertical' if it comes from the top or bottom side.
            - 'horizontal' if it comes from the left or right side.
        
        '''
        x0, y0, x1, y1 = lazor
        if y1 % 2 == 0:  
            return 'vertical'
        elif x1 % 2 == 0: 
            return 'horizontal'
        else:
            return None  
    

    def display_board(self):
        """
        Display the current blocks_ layout for debugging.
        """
        print("\nCurrent Block Layout:")
        for row in self.blocks_:
            print(" | ".join(f"{block.category}" for block in row))
            print("-" * (self.width * 4))  
            
    def add_lazor(self, x0, y0, x1, y1):
        '''
        Append new lazor to the list 'all_lazor' that stores all the lazors.
        '''
        self.all_lazor.append((x0, y0, x1, y1))

    def add_original_blocks(self):
        '''
        Use the original board information to create blocks instances and store them in self.blocks_.
        '''
        blocks = []
        for r in range(self.height):
            row = []
            for c in range(self.width):
                char = self.original_board[r][c]
                if char == 'x':
                    block = Blocks(category="X", position=(r, c))
                elif char == 'o':
                    block = Blocks(category="O", position=(r, c))
                elif char in ['A', 'B', 'C']:
                    block = Blocks(category=char, position=(r, c))
                else:
                    block = Blocks(category="O", position=(r, c))
                row.append(block)
            blocks.append(row)
        return blocks

    def place_blocks(self, position, block_type):
        '''
        Place blocks at a given location.
        '''
        x, y = position
        if not (0 <= y < self.height and 0 <= x < self.width):
            raise ValueError("Out of border")

        if self.original_board[y][x] != 'o':
            raise ValueError(f"Position {position} is already taken")
        
        if isinstance(self.original_blocks[y][x], Blocks) and self.original_blocks[y][x].category != 'O':
            raise ValueError(f"Position {position} is already occupied by {self.original_blocks[y][x].category}.")
        
        block = Blocks(block_type, position) 
        self.blocks_[y][x] = block  

    def generate_initial_lazor(self):
        '''
        Generate the initial lazor paths from the starting positions and directions.
        '''
        for (px, py), (dx, dy) in zip(self.lazor_position, self.lazor_direction):
            # Calculate the block to interact with the lazor initially
            if px % 2 == 0:  # From left or right side
                if dx > 0: 
                    block_x = px // 2
                    block_y = (py - 1) // 2
                else:
                    block_x = px // 2 - 1
                    block_y = (py - 1) // 2
            else:  # From upper or bottom side
                if dy > 0:
                    block_y = py // 2
                    block_x = (px - 1) // 2
                else:
                    block_y = py // 2 - 1
                    block_x = (px - 1) // 2

            current_block = self.blocks_[block_y][block_x]
            type = current_block.category

            if type == 'A':
                if px % 2 == 0:
                    dx_ = -dx
                    px_, py_ = px + dx_, py + dy
                else:
                    dy_ = -dy
                    px_, py_ = px + dx, py + dy_
                self.initial_lazor.append((px, py, px_, py_))

            elif type == 'C':
                if px % 2 == 0:
                    dx_ = -dx
                    px_, py_ = px + dx_, py + dy
                else:
                    dy_ = -dy
                    px_, py_ = px + dx, py + dy_
                self.initial_lazor.append((px, py, px_, py_))
                px_, py_ = px + dx, py + dy
                self.initial_lazor.append((px, py, px_, py_))
            
            elif type == 'O' or type == 'X':
                self.initial_lazor.append((px, py, px + dx, py + dy))

    def clear_blocks(self):
        '''
        clear blocks_ to default state
        '''
        self.blocks_ = copy.deepcopy(self.original_blocks)

    def get_interact_block(self, lazor):
        '''
        Determine the position of the block interacting with the lazor segment,
        based on the direction of the lazor and entry side.
        

        Returns:
            tuple: (block_x, block_y) representing the coordinates of the interacting block
        '''
        x0, y0, x1, y1 = lazor
        dx, dy = x1 - x0, y1 - y0  

        # Determine block based on lazor direction and entry side
        entry_side = self.vtc_or_hrz(lazor)
        if entry_side == 'vertical':
            if dy > 0:  
                block_y, block_x = y1 // 2, (x1 - 1) // 2
            else:      
                block_y, block_x = y1 // 2 - 1, (x1 - 1) // 2
        elif entry_side == 'horizontal':
            if dx > 0:  
                block_y, block_x = (y1 - 1) // 2, x1 // 2
            else:       
                block_y, block_x = (y1 - 1) // 2, x1 // 2 - 1
        else:
            raise ValueError("Lazor direction is undetermined; check vtc_or_hrz output.")

        if 0 <= block_y < self.height and 0 <= block_x < self.width:
            return block_y, block_x
        else:
            return None  # Out of board boundaries

    def check_targets_reached(self):
        """
        Checks if all target positions are hit by at least one lazor path.

        Returns:
            bool: True if all targets are reached
        """
        # Get the set of target positions for quick lookup
        target_set = set(self.target)

        # Get all points that lazors pass through
        hit_positions = set()
        for path in self.all_lazor:
            x0, y0, x1, y1 = path
            hit_positions.add((x1, y1))  # Add the endpoint of each lazor segment
            hit_positions.add((x0, y0))

        # Check if each target is in the hit_positions
        return target_set.issubset(hit_positions)




        
