class Board:
    '''
    Store the board as a class
    lazors are stored in single unit in the format of (x0, y0, x1, y1)

    '''

    def __init__(self, orignal_board):
        self.original_board = orignal_board
        self.height = len(self.original_board) 
        self.width = len(self.original_board[0])

        self.board_dic = self.board_transfer()
        self.blocks_ = self.add_original_blocks()
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

    def add_original_blocks(self):
        blocks_ = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for r in range(self.height):
            for c in range(self.width):
                # Map 'o' to None and 'x' to 0
                if self.original_board[r][c] == 'o':
                    blocks_[r][c] = 1
                elif self.original_board[r][c] == 'x':
                    blocks_[r][c] = 0
        return blocks_

    def display_board(self):
        '''
        Display the board for debugging or gameplay purposes.
        '''
        for row in self.board_dic:
            print(" | ".join(f"{cell['lazor_status']}" for cell in row))
            print("-" * (self.width * 4))  # Adjust for visual separation

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