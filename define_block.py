class Block:
    def __init__(self, block_type):
        self.type = block_type

    def get_new_direction(self, point, direction):
        new_direction = []

        # Reflect block behavior
        if self.type == 'A':
            if point[0] % 2 == 0:
                new_direction = [direction[0] * (-1), direction[1]]
            else:
                new_direction = [direction[0], direction[1] * (-1)]

        # Opaque block behavior
        elif self.type == 'B':
            new_direction = []

        # Refract block behavior
        elif self.type == 'C':
            if point[0] % 2 == 0:
                new_direction = [direction[0], direction[1],
                                 direction[0] * (-1), direction[1]]
            else:
                new_direction = [direction[0], direction[1],
                                 direction[0], direction[1] * (-1)]

        # Crystal block behavior
        elif self.type == 'D':
            if point[0] % 2 == 0:
                new_direction = [2, 0, direction[0], direction[1]]
            else:
                new_direction = [0, 2, direction[0], direction[1]]

        # Blank or unavailable space
        elif self.type == 'o' or self.type == 'x':
            new_direction = direction

        return new_direction
