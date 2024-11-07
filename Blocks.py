class Blocks:
    """
    Each block is defined as a class instance.

    """

    def __init__(self, category=None, position=None):
        """
        Initializes a block with category and position.

        Parameters:
            category (str): The type of the block.
            position (tuple): The (x, y) position of the block.
        """
        self.category = category
        self.position = position

    def vtc_or_hrz(self, lazor):
        """
        Identifies the side from which the lazor approaches the block.

        Parameters:
            lazor (tuple): Lazor unit in the format (x0, y0, x1, y1).

        Returns:
            str: 
                -'vertical' if lazor approaches from top/bottom
                -'horizontal' from left/right
                - None 
        """
        x0, y0, x1, y1 = lazor
        if y1 % 2 == 0:
            flag = 'vertical'
        elif x1 % 2 == 0:
            flag = 'horizontal'
        else:
            flag = None
        return flag

    def get_direction(self, lazor):
        """
        Calculates the direction vector of the lazor.

        """
        x0, y0, x1, y1 = lazor
        dx = x1 - x0
        dy = y1 - y0
        return dx, dy

    def straight_lazor(self, lazor):
        """
        Lazor goes in straight line if no block to interact

        Parameters:
            lazor (tuple): Lazor unit in the format (x0, y0, x1, y1).

        Returns:
            tuple: New lazor in the format (x0_, y0_, x1_, y1_).
        """
        x0, y0, x1, y1 = lazor
        dx, dy = self.get_direction(lazor)
        x0_, y0_ = x1, y1
        x1_, y1_ = x0_ + dx, y0_ + dy
        return (x0_, y0_, x1_, y1_)

    def reflect(self, lazor):
        """
        Reflects the lazor off the block.

        Parameters:
            lazor (tuple): Lazor segment coordinates in the format (x0, y0, x1, y1).

        Returns:
            tuple: New lazor coordinates after reflection.
        """
        x0, y0, x1, y1 = lazor
        dx, dy = self.get_direction(lazor)
        x0_, y0_ = x1, y1
        if self.vtc_or_hrz(lazor) == 'vertical':
            dy = -dy
        elif self.vtc_or_hrz(lazor) == 'horizontal':
            dx = -dx
        x1_ = x0_ + dx
        y1_ = y0_ + dy
        return (x0_, y0_, x1_, y1_)

    def opaque(self, lazor):
        """
        Blocks the lazor completely.

        """
        return None

    def refract(self, lazor):
        """
        Splits the lazor into reflected and straight paths.
        """
        new_lazor_1 = self.reflect(lazor)
        new_lazor_2 = self.straight_lazor(lazor)
        return new_lazor_1, new_lazor_2

    def alert(self):
        """
        For debugging
        """
        print("Alert: No interaction detected with the block.")
        return None

    def lazor_interact(self, lazor):
        """
        Determines the lazor's interaction with the block based on its category.
        """
        if self.category == 'A':  # Reflective block
            return [self.reflect(lazor)]
        elif self.category == 'B':  # Opaque block
            return [self.opaque(lazor)]
        elif self.category == 'C':  # Refractive block
            return list(self.refract(lazor))
        elif self.category == 'O' or self.category == 'X':  # Empty or blocked location
            return [self.straight_lazor(lazor)]
        else:
            return [self.alert()]
