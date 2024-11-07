import numpy as np
import pandas as pd
import matplotlib as plt

class Grid(object):

    def __init__(self, original_grid):
        self.list_grid = None
        self.length = len(original_grid)
        self.width = len(original_grid[0])
        self.original_grid = original_grid

    def generate_grid(self, list_grid, position):
        self.list_grid = list_grid
        for row in range(len(self.original_grid)):
            for column in range(len(self.original_grid[0])):
                if [row, column] not in position:
                    if self.original_grid[row][column] != 'x':
                        self.original_grid[row][column] = list_grid.pop(0)
        return self.original_grid

