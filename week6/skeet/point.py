class Point:
    def __init__(self,x=None,y=None):
        if x == None and y == None:
            self.x = 0
            self.y = 0
        else:
            self.x = x
            self.y = y
    def get_center_x(self):
        return self.x
    def get_center_y(self):
        return self.y
    def set_y_center(self,y):
        self.y = y
    def set_x_center(self,x):
        self.x = x
    def add_x(self, dx):
        self.set_x_center(self.x + dx)
    def add_y(self, dy):
        self.set_y_center(self.y + dy)