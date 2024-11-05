from Blocks import Blocks

class Board:



    '''
    Store the board as a class
    lazors are stored in single unit in the format of (x0, y0, x1, y1)
    
    There are two grids:
    1- m*n to store blocks
    2- (2m-1) *(2n-1) to store lazor and target


    '''

    def __init__(self, orignal_board):
        self.original_board = orignal_board
        self.height = len(self.original_board) 
        self.width = len(self.original_board[0])

        self.board_dic = self.board_transfer()
        
        #where the blocks are stored in
        self.original_blocks = self.add_original_blocks()
        #deep copy a block map to store the new map with blocks solutions
        self.blocks_ = [row[:] for row in self.original_blocks]

        self.all_lazor = []
        self.inital_lazor = [] #初始的激光段,不允许在这一块放置block
        
        self.target = []

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

            self.inital_lazor.append((x0, y0, x1, y1))

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
        if not (0 <= x < self.height and 0 <= y < self.width):
            raise ValueError("out of border")

        if self.original_board[x][y] != 'o':
            raise ValueError(f"position {position} is already taken")
        
        if isinstance(self.original_blocks[x][y], Blocks) and self.original_blocks[x][y].category != 'O':
            raise ValueError(f"Position {position} is already occupied by {self.original_blocks[x][y].category}.")
        
        block = Blocks(block_type, position)  # 创建新的块对象
        self.blocks_[x][y] = block  # 更新 blocks_ 数组
        print(f"Successfully placed block of type '{block_type}' at position {position}.")
