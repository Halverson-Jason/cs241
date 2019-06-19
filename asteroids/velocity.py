class Velocity:
    def __init__(self,dx=0.0,dy=0.0):
        self.velocity_dx = dx
        self.velocity_dy = dx
    def copy(self):
        return Velocity(self.dx,self.dy)

    @property
    def dx(self):
        return self.velocity_dx
    @dx.setter
    def dx(self,dx):
        self.velocity_dx = dx
    @property
    def dy(self):
        return self.velocity_dy
    @dy.setter
    def dy(self,dy):
        self.velocity_dy = dy
    @property
    def vector(self):
        return (self.velocity_dx,self.velocity_dy)
    @vector.setter
    def vector(self, coordinates):
        self.velocity_dx, self.velocity_dy = coordinates