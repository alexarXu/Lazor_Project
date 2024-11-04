class Blocks:
    '''
    每个block都由一个类定义
    '''
    def __init__(self, category, position):
        self.category = category
        self.position = position
    
    def vtc_or_hrz(self, lazor):
        '''
        to identify which side is the lazor from:
            1- upper and bottom side: vertical(True)
            2- left and right side: horizonal(False)
        '''
        x0, y0, x1, y1 = lazor
        if y1 // 2 == 0:
            flag = 'vertical'
        elif x1 // 2 == 0:
            flag = 'horizonal'
        else:
            flag = None
        
        return flag

    def get_direction(self, lazor):
        x0, y0, x1, y1 = lazor
        dx = x1 - x0
        dy = y1 - y0
        return dx, dy

    def reflect(self, lazor):
        x0, y0, x1, y1 = lazor
        dx, dy = self.get_direction(lazor)
        x0_, y0_ = x1, y1 #new lazor
        if self.vtc_or_hrz(lazor) == 'vertical':
            dy = 0 - dy
        elif self.vtc_or_hrz(lazor) == 'horizonal':
            dx = 0 - dx
        x1_ = x0_ + dx
        y1_ = y0_ + dy

        new_lazor = [x0_, y0_, x1_, y1_]
        return new_lazor

    def opaque(self, lazor):
        """
        """
        return None

    def refract(self, lazor):
        new_lazor_1 = self.reflect(lazor)
        return new_lazor_1

    def alert():
        return None

    def lazor_interact(self, lazor):
        '''
        Assume that the lazor must interact with the block
        single_lazor is a list with format as(px, py, dx, dy)

        output:
            新的line_lazor
        '''

        self.alert() #if not interact, print alert

        if self.category == 'A':
            new_lazor = self.reflect(lazor)
        
        elif self.category == 'B':
            new_lazor = self.opaque(lazor)

        if self.category == 'C':
            new_lazor = self.refract(lazor)

   

