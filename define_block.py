import numpy as np
import pandas as pd
import matplotlib as plt

class Block:
    def __init__(self, block_type, laserpoint, laserdirection):
        self.block_type = block_type
        self.laserpoint = laserpoint
        self.laserdirection = laserdirection

    def direction_change(self):
        direction = []
        # A - reflect block: laser will reflect when hit this block
        # directiton changes: (vx, vy) -> (-vx, -vy)
        if self.block_type == 'A':
            if self.laserpoint[0] % 2 == 0:
                direction = [self.laserdirection[0] * (-1), self.laserdirection[1]]
            else:
                direction = [self.laserdirection[0], self.laserdirection[1] * (-1)]
        # B - opaque block: laser will stop when hit this block
        # direction changes: (vx, vy) -> None
        elif self.block_type == 'B':
            return None
        # C - refract block: laser will reflect and create a new laser passed when hit this block
        # direction changes: (vx, vy) -> (vx, vy) + (-vx, -vy)
        elif self.block_type == 'C':
            if self.laserpoint[0] % 2 == 0:
                direction = [[self.laserdirection[0], self.laserdirection[1]],
                             [self.laserdirection[0] * (-1), self.laserdirection[1]]]
            else:
                direction = [[self.laserdirection[0], self.laserdirection[1]],
                             [self.laserdirection[0], self.laserdirection[1] * (-1)]]
        # If played with Lazor you will know what is this lol:
        # D - crystal block: laser will pass through the block horizontally or vertically, then keep the original directions
        # direction changes: still (vx, vy)
        elif self.block_type == 'D':
            direction = self.laserdirection
        # 'o', 'x' - laser will pass through the block and remain the original directions
        # direction changes: still(vx, vy)
        elif self.block_type == 'o' or self.block_type == 'x':
            direction = self.laserdirection
        return direction
