from define_block import Block
from utlis import *

class Lazor:
    def __init__(self, grid, lazor_list, target_list):
        '''
        This function initializes the laser.
        ***Parameters***
        grid: 2D list, the grid of the game.
        lazor_list: 2D list, the position and direction of the lazor.
        target_list: 2D list, the target points.
        '''
        self.grid = grid
        self.lazor_list = lazor_list
        self.target_list = target_list

    def check_position(self, current_lazor_position, direction):
        '''
        This function checks if the position is valid.
        You can also use the function check_if_the_point_in_grid from utlis.py.
        ***Parameters***
        current_lazor_position: list, the position of the lazor.
        direction: list, the direction of the lazor.
        ***Return***
        bool, True if the position is invalid, False otherwise
        '''
        width = len(self.grid[0])
        length = len(self.grid)
        x, y = current_lazor_position

        if (x < 0 or x >= width or y < 0 or y >= length or
                direction is None or
                x + direction[0] < 0 or x + direction[0] >= width or  # Check if the next position is out of the grid
                y + direction[1] < 0 or y + direction[1] >= length):  # Same as above
            return True
        return False

    def block_reflect(self, point, direction):
        '''
        This function that actually describes the interaction between the lazor and the blocks.
        By calling the Block class, we can get the new direction of the lazor.
        ***Parameters***
        point: list, the position of the lazor.
        direction: list, the direction of the lazor.
        ***Return***
        list, the new direction of the lazor.
        '''
        x1, y1 = point[0], point[1] + direction[1]
        x2, y2 = point[0] + direction[0], point[1]

        # Determine which block to interact with
        block_type = self.grid[y1][x1] if point[0] % 2 == 1 else self.grid[y2][x2]

        # Create a Block instance and get new direction
        block = Block(block_type)
        new_direction = block.get_new_direction(point, direction)
        
        return new_direction

    def lazor_path(self):
        '''
        This function generates the path of the lazor.
        ***Return***
        list, the path of the lazor.
        '''
        result = []
        lazor_paths = [[lazor] for lazor in self.lazor_list]

        for _ in range(100):  # Limiting to 100 steps for termination
            for path in lazor_paths:
                x, y, dx, dy = path[-1]
                coord = [x, y]
                direction = [dx, dy]

                if self.check_position(coord, direction):
                    continue

                next_step = self.block_reflect(coord, direction)

                if not next_step:
                    path.append([x, y, 0, 0])
                    if coord in self.target_list and coord not in result:
                        result.append(coord)

                elif len(next_step) == 2:
                    direction = next_step
                    coord = [coord[0] + direction[0], coord[1] + direction[1]]
                    path.append([coord[0], coord[1], direction[0], direction[1]])
                    if coord in self.target_list and coord not in result:
                        result.append(coord)

                elif len(next_step) == 4:
                    if next_step[0] == 0 or next_step[0] == 2:
                        direction = next_step
                        coord = [coord[0] + direction[0], coord[1] + direction[1]]
                        path.append([coord[0], coord[1], direction[2], direction[3]])
                        if coord in self.target_list and coord not in result:
                            result.append(coord)
                    else:
                        direction = next_step
                        new_lazor1 = [coord[0] + direction[0], coord[1] + direction[1], direction[0], direction[1]]
                        lazor_paths.append([new_lazor1])

                        coord = [coord[0], coord[1]]
                        path.append([coord[0], coord[1], direction[2], direction[3]])
                        if coord in self.target_list and coord not in result:
                            result.append(coord)

        if len(result) == len(self.target_list):
            return lazor_paths
        return 0