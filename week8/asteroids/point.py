class Point:
    def __init__(self,x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    @property
    def center_x(self):
        return self.x
    @center_x.setter
    def center_x(self,dx):
        self.x = self.x + dx

    @property
    def center_y(self):
        return self.y
    @center_y.setter
    def center_y(self,dy):
        self.y = self.y + dy