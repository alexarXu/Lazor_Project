'''
This file defines the grid class, which is used to generate the grid based on the original grid and the position of the obstacles.
'''
class Grid(object):
    def __init__(self, original_grid):
        '''
        This function initializes the grid class.
        '''
        self.list_grid = None
        self.length = len(original_grid)
        self.width = len(original_grid[0])
        self.original_grid = original_grid

    def generate_grid(self, list_grid, position):
        '''
        This function generates the grid based on the original grid and the position of the obstacles.
        ***Parameters***
        list_grid: list, the list of blocks in the grid.
        position: list, the position of the obstacles.
        ***Return***
        original_grid: 2D list, the generated grid.
        '''
        self.list_grid = list_grid
        for row in range(len(self.original_grid)):
            for column in range(len(self.original_grid[0])):
                if [row, column] not in position:
                    if self.original_grid[row][column] != 'x':
                        self.original_grid[row][column] = list_grid.pop(0)
        return self.original_grid