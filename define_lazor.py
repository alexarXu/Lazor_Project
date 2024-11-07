import numpy as np
import pandas as pd
from define_block import Block
from utlis import *


class Laser(object):

    def __init__(self, grid, laserpoints, laserdirections, targetpoints):
        self.grid = grid
        self.laserpoints = laserpoints
        self.laserdirections = laserdirections
        self.targetpoints = targetpoints   
    
    def laser_reflect(self, hitpoint, hitdirection):
        '''
        This function to reflect the laser when it hits the block.
        ***Parameters***
        hitpoint: list, the point where the laser hits the block.
        hitdirection: list, the direction of the laser when it hits the block.
        ***Returns***
        new_direction: list, the new direction of the laser.
        '''
        new_x1 = hitpoint[0]
        new_y1 = hitpoint[1] + hitdirection[1]
        new_x2 = hitpoint[0] +hitdirection[0] 
        new_y2 = hitpoint[1]

        if hitpoint[0] & 1 == 1:
            block_type = self.grid[new_y1][new_x1]
        else:
            block_type = self.grid[new_x2][new_y2]

        block = Block(block_type, hitpoint, hitdirection)
        return block.direction_change()
    

    def laser_out_of_grid(self, laserpoint, direction):
        '''
        This function checks if the laser is out of the grid.
        ***Parameters***
        laserpoint: list, the position of the lazor.
        direction: list, the direction of the lazor.
        ***Returns***
        True if the lazor is out of the grid, False otherwise.
        '''
        new_x = laserpoint[0] + direction[0]
        new_y = laserpoint[1] + direction[1]
        return not check_if_the_point_in_grid(laserpoint, self.grid) or \
               not check_if_the_point_in_grid([new_x, new_y], self.grid)


    def update_laser_state(self, laserpoints, laserdirections, next_step, coordination, k, result):
        """
        This function updates the state of the laser based on the next step.
        ***Parameters***
        laserpoints: list, the positions of the lazors.
        laserdirections: list, the directions of the lazors.
        next_step: list, the next step of the lazor.
        coordination: list, the position of the lazor.
        k: int, the index of the lazor.
        result: list, the positions of the target points that have been hit.
        ***Returns***
        laserpoints: list, the updated positions of the lazors.
        laserdirections: list, the updated directions of the lazors.
        result: list, the updated positions of the target points that have been hit.
        """
        if not next_step:
            # Stop the laser
            laserpoints[k] = coordination
            laserdirections[k] = [0, 0]
            if coordination in self.targetpoints and coordination not in result:
                result.append(coordination)
        elif len(next_step) == 2:  # Single direction change
            direction = next_step
            coordination = [coordination[0] + direction[0], coordination[1] + direction[1]]
            laserpoints[k] = coordination
            laserdirections[k] = direction
            if coordination in self.targetpoints and coordination not in result:
                result.append(coordination)
        elif len(next_step) == 4:  # Split laser
            direction = next_step
            coordination_new_lazor1 = [coordination[0] + direction[0], coordination[1] + direction[1]]
            coordination_new_lazor2 = [coordination[0], coordination[1]]

            # Add the new lasers to the list
            laserpoints.append(coordination_new_lazor1)
            laserdirections.append([direction[0], direction[1]])

            laserpoints[k] = coordination_new_lazor2
            laserdirections[k] = [direction[2], direction[3]]
            coordination = coordination_new_lazor2
            if coordination in self.targetpoints and coordination not in result:
                result.append(coordination)

        return laserpoints, laserdirections, result
    

    def laser_path_validation(self):
        """
        Main method to simulate the laser paths and check if they hit the target.
        :return: Updated laser paths or 0 if not all targets are reached.
        """
        result = []
        for _ in range(100):  # Maximum 50 iterations to simulate the laser path
            for k in range(len(self.laserpoints)):
                laserpoint = self.laserpoints[k]
                direction = self.laserdirections[k]

                if self.laser_out_of_grid(laserpoint, direction):
                    continue  # Skip if the laser is out of the grid

                next_step = self.laser_reflect(laserpoint, direction)

                # Update the laser state based on the next step
                self.laserpoints, self.laserdirections, result = self.update_laser_state(
                    self.laserpoints, self.laserdirections, next_step, laserpoint, k, result
                )

        # If all target points are hit, return the final state of the laser paths
        if len(result) == len(self.targetpoints):
            return self.laserpoints, self.laserdirections
        else:
            return 0