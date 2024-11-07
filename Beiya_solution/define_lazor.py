from define_block import Block
from utlis import *

class Lazor:
    def __init__(self, grid, lazor_list, hole_list):
        self.grid = grid
        self.lazor_list = lazor_list
        self.hole_list = hole_list

    def check_position(self, lazor_coordinate, direction):
        width = len(self.grid[0])
        length = len(self.grid)
        x, y = lazor_coordinate

        # Determine if the position is within the grid
        if (x < 0 or x >= width or y < 0 or y >= length or
                direction is None or
                x + direction[0] < 0 or x + direction[0] >= width or
                y + direction[1] < 0 or y + direction[1] >= length):
            return True
        else:
            return False

    def block_reflect(self, point, direction):
        x1, y1 = point[0], point[1] + direction[1]
        x2, y2 = point[0] + direction[0], point[1]

        # Determine which block to interact with
        if point[0] % 2 == 1:
            block_type = self.grid[y1][x1]
        else:
            block_type = self.grid[y2][x2]

        # Create a Block instance and get new direction
        block = Block(block_type)
        new_direction = block.get_new_direction(point, direction)
        
        return new_direction

    def lazor_path(self):
        result = []
        lazor_list = [[lazor] for lazor in self.lazor_list]

        for _ in range(50):  # Limiting to 50 steps for termination
            for k in range(len(lazor_list)):
                x, y, dx, dy = lazor_list[k][-1]
                coord = [x, y]
                direction = [dx, dy]

                if self.check_position(coord, direction):
                    continue

                next_step = self.block_reflect(coord, direction)

                if not next_step:
                    lazor_list[k].append([x, y, 0, 0])
                    if coord in self.hole_list and coord not in result:
                        result.append(coord)

                elif len(next_step) == 2:
                    direction = next_step
                    coord = [coord[0] + direction[0], coord[1] + direction[1]]
                    lazor_list[k].append([coord[0], coord[1], direction[0], direction[1]])
                    if coord in self.hole_list and coord not in result:
                        result.append(coord)

                elif len(next_step) == 4:
                    if next_step[0] == 0 or next_step[0] == 2:
                        direction = next_step
                        coord = [coord[0] + direction[0], coord[1] + direction[1]]
                        lazor_list[k].append([coord[0], coord[1], direction[2], direction[3]])
                        if coord in self.hole_list and coord not in result:
                            result.append(coord)
                    else:
                        direction = next_step
                        new_lazor1 = [coord[0] + direction[0], coord[1] + direction[1], direction[0], direction[1]]
                        lazor_list.append([new_lazor1])

                        coord = [coord[0], coord[1]]
                        lazor_list[k].append([coord[0], coord[1], direction[2], direction[3]])
                        if coord in self.hole_list and coord not in result:
                            result.append(coord)

        if len(result) == len(self.hole_list):
            return lazor_list
        else:
            return 0
