class Blocks:
    '''
    每个block都由一个类定义
    '''
    def __init__(self, category = None, position = None):
        '''
        category:
        A- reflect
        B- opaque
        C- refract
        O-empty
        X-not allowed
        '''
        self.category = category
        self.position = position
    
    def vtc_or_hrz(self, lazor):
        '''
        to identify which side is the lazor from:
            1- upper and bottom side: vertical(True)
            2- left and right side: horizonal(False)
        '''
        x0, y0, x1, y1 = lazor
        if y1 % 2 == 0:
            flag = 'vertical'
        elif x1 % 2 == 0:
            flag = 'horizonal'
        else:
            flag = None
        
        return flag

    def get_direction(self, lazor):
        x0, y0, x1, y1 = lazor
        dx = x1 - x0
        dy = y1 - y0
        return dx, dy

    def straight_lazor(self, lazor):
        '''
        a lazor travels in straight
        '''
        x0, y0, x1, y1 = lazor
        dx, dy = self.get_direction(lazor)
        x0_, y0_ = x1, y1
        x1_, y1_ = x0_ + dx, y0_ + dy

        return (x0_, y0_, x1_, y1_)

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

        new_lazor = (x0_, y0_, x1_, y1_)
        return new_lazor

    def opaque(self, lazor):
        """
        """
        return None

    def refract(self, lazor):
        new_lazor_1 = self.reflect(lazor)
        new_lazor_2 = self.straight_lazor(lazor)
        return new_lazor_1, new_lazor_2

    def alert(self):
        '''
        '''
        print("Alert: No interaction detected with the block.")
        return None


    def lazor_interact(self, lazor):
        '''
        Assume that the lazor must interact with the block
        single_lazor is a list with format as(px, py, dx, dy)

        output:
            新的line_lazor
        '''

        if self.category == 'A':  # Reflective block
            return [self.reflect(lazor)]  # 返回一个包含反射路径元组的列表
        elif self.category == 'B':  # Opaque block
            return [self.opaque(lazor)]  # 返回包含一个 None 元素的列表，表示激光被阻挡
        elif self.category == 'C':  # Refractive block
            return list(self.refract(lazor))  # 返回包含折射和反射路径的列表
        elif self.category == 'O' or self.category == 'X':  # Empty space, lazor passes through unchanged
            return [self.straight_lazor(lazor)]
        else:
            return [self.alert()]

   

