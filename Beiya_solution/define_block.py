class Block:
    def __init__(self, block_type):
        self.type = block_type

    def get_new_direction(self, point, direction):
        '''
        This function returns the new direction of the lazor after hitting the block.
        ***Parameters***
        point: list, the point where the lazor hits the block.
        direction: list, the direction of the lazor.
        ***Returns***
        new_direction: list, the new direction of the lazor.
        '''
        new_direction = []

        # Reflect block behavior
        # If the point is even, the direction is reversed
        # If the point is odd, the direction is not reversed
        if self.type == 'A':
            if point[0] % 2 == 0:
                new_direction = [direction[0] * (-1), direction[1]]
            else:
                new_direction = [direction[0], direction[1] * (-1)]

        # Opaque block behavior
        # The lazor will be stopped here
        elif self.type == 'B':
            new_direction = []

        # Refract block behavior
        # The refracted lazor will continue in the same direction and add a new direction
        # The new direction is like the reflection block
        elif self.type == 'C':
            if point[0] % 2 == 0:
                new_direction = [direction[0], direction[1],
                                 direction[0] * (-1), direction[1]]
            else:
                new_direction = [direction[0], direction[1],
                                 direction[0], direction[1] * (-1)]

        # Crystal block behavior 
        # This kind is just for fun and not used in the board, but if you have played the game you will know what I mean
        # The lazor will be refracted and continue in the same direction
        # The new direction is same as the original direction
        elif self.type == 'D':
            if point[0] % 2 == 0:
                new_direction = [2, 0, direction[0], direction[1]]
            else:
                new_direction = [0, 2, direction[0], direction[1]]

        # Blank or unavailable space
        # The lazor will continue in the same direction
        elif self.type == 'o' or self.type == 'x':
            new_direction = direction

        return new_direction
