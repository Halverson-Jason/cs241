class Velocity:
    def __init__(self,dx=0.0,dy=0.0):
        self.dx = dx
        self.dy = dx
    @property
    def dx(self):
        return self.dx
    @dx.setter
    def dx(self,dx):
        self.dx = dx
    @property
    def dy(self):
        return self.dy
    @dy.setter
    def dy(self,dy):
        self.dy = dy