from Blocks import Blocks
import copy

class Board:
    '''
    Store the board as a class
    lazors are stored in single unit in the format of (x0, y0, x1, y1)
    
    There are two grids:
    1- m*n to store blocks
    2- (2m-1) *(2n-1) to store lazor and target


    '''

    def __init__(self, orignal_board, A_num, B_num, C_num):
        self.original_board = orignal_board
        self.height = len(self.original_board) 
        self.width = len(self.original_board[0])

        self.board_dic = self.board_transfer()
        
        #where the blocks are stored in
        self.original_blocks = self.add_original_blocks()
        #deep copy a block map to store the new map with blocks solutions
        self.blocks_ = copy.deepcopy(self.original_blocks)

        self.all_lazor = []
        self.initial_lazor = [] #初始的激光段,不允许在这一块放置block
        
        self.target = []
        self.A_num, self.B_num, self.C_num = A_num, B_num, C_num


    def board_transfer(self):
        '''
        transfer the board from full a o and x into a list
        '''
        #calculate the size of board
        height = 2 * self.height + 1
        width = 2 * self.width + 1
        board_dic = [[{'lazor_status': None, 'block_status': None} for _ in range(width)] for _ in range(height)]

        return board_dic

    
    def display_board(self):
        """
        Display the current blocks_ layout for debugging or gameplay purposes.
        """
        print("\nCurrent Block Layout:")
        for row in self.blocks_:
        # 逐行打印每个块的类别
            print(" | ".join(f"{block.category}" for block in row))
            print("-" * (self.width * 4))  # 使用分隔线分隔行

            
    def add_lazor(self, x0, y0, x1, y1):
        '''
        append new lazor to the tuple 'all_lazor' that store all the lazors
        '''
        self.all_lazor.append((x0, y0, x1, y1))
    
    def pop_lazor(self):
        '''
        
        '''
        self.all_lazor.pop()

    def get_original_lazor(self, lazor_position, lazor_direction):
        '''
        calculate the initial lazor unit from the given lazor source
        '''
        for index in range(len(lazor_position)):
            x0, y0 = lazor_position[index]
            dx, dy = lazor_direction[index]
            x1, y1 = x0 + dx, y0 + dy

            self.initial_lazor.append((x0, y0, x1, y1))

    def push_target(self, target):
        for index in range(len(target)):
            x, y = target[index]

            self.target.append((x, y))

    def add_original_blocks(self):
        '''
        
        '''
        # board = self.original_board
        # blocks = [[Blocks(position=(r, c)) for c in range(self.width)] for r in range(self.height)]
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
        
        x, y = position
        if not (0 <= y < self.height and 0 <= x < self.width):
            raise ValueError("out of border")

        if self.original_board[y][x] != 'o':
            raise ValueError(f"position {position} is already taken")
        
        if isinstance(self.original_blocks[y][x], Blocks) and self.original_blocks[y][x].category != 'O':
            raise ValueError(f"Position {position} is already occupied by {self.original_blocks[y][x].category}.")
        
        block = Blocks(block_type, position)  # 创建新的块对象
        self.blocks_[y][x] = block  # 更新 blocks_ 数组
        #print(f"Successfully placed block of type '{block_type}' at position {position}.")

    def vtc_or_hrz(self, lazor):
        '''
        Identify the side from which the lazor approaches:
            - 'vertical' if it comes from the top or bottom side.
            - 'horizontal' if it comes from the left or right side.
        
        Parameters:
            lazor (tuple): Current lazor segment coordinates in the format (x0, y0, x1, y1)
        
        Returns:
            str: 'vertical', 'horizontal', or None if undetermined.
        '''
        x0, y0, x1, y1 = lazor
        if y1 % 2 == 0:  
            return 'vertical'
        elif x1 % 2 == 0: 
            return 'horizontal'
        else:
            return None  # Diagonal or undetermined movement

    def get_interact_block(self, lazor):
        '''
        Determine the coordinates of the block interacting with the lazor segment,
        based on the direction of the lazor and entry side.
        
        Parameters:
            lazor (tuple): The current lazor segment coordinates in the format (x0, y0, x1, y1)

        Returns:
            tuple: (block_x, block_y) representing the coordinates of the interacting block
        '''
        x0, y0, x1, y1 = lazor
        dx, dy = x1 - x0, y1 - y0  # Calculate direction

        # Determine block based on lazor direction and entry side
        entry_side = self.vtc_or_hrz(lazor)
        if entry_side == 'vertical':
            # Adjust block position based on vertical approach
            if dy > 0:  # Moving down
                block_y, block_x = y1 // 2, (x1 - 1) // 2
            else:       # Moving up
                block_y, block_x = y1 // 2 - 1, (x1 - 1) // 2
        elif entry_side == 'horizontal':
            # Adjust block position based on horizontal approach
            if dx > 0:  # Moving right
                block_y, block_x = (y1 - 1) // 2, x1 // 2
            else:       # Moving left
                block_y, block_x = (y1 - 1) // 2, x1 // 2 - 1
        else:
            raise ValueError("Lazor direction is undetermined; check vtc_or_hrz output.")

        # else:
        #     # If undetermined, use diagonal movement rules
        #     if dx == 1 and dy == 1:
        #         block_x, block_y = (x1 - 1) // 2, (y1 - 1) // 2
        #     elif dx == -1 and dy == -1:
        #         block_x, block_y = (x1 + 1) // 2, (y1 + 1) // 2
        #     elif dx == 1 and dy == -1:
        #         block_x, block_y = (x1 - 1) // 2, (y1 + 1) // 2
        #     elif dx == -1 and dy == 1:
        #         block_x, block_y = (x1 + 1) // 2, (y1 - 1) // 2
        #     else:
        #         raise ValueError(f"Unexpected lazor direction ({dx}, {dy}).")

        # Check if the block coordinates are within board boundaries
        if 0 <= block_y < self.height and 0 <= block_x < self.width:
            return block_y, block_x
        else:
            return None  # Out of board boundaries

    def check_targets_reached(self):
        """
        Checks if all target positions are hit by at least one lazor path.

        Returns:
            bool: True if all targets are reached by lazor paths, False otherwise.
        """
        # Get the set of target positions for quick lookup
        target_set = set(self.target)

        # Get all points that lazors pass through
        hit_positions = set()
        for path in self.all_lazor:
            x0, y0, x1, y1 = path
            hit_positions.add((x1, y1))  # Add the endpoint of each lazor segment

        # Check if each target is in the hit_positions
        return target_set.issubset(hit_positions)

    def clear_blocks(self):
        '''
        clear blocks_ to default state
        '''
        self.blocks_ = copy.deepcopy(self.original_blocks)
