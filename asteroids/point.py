class Point:
    def __init__(self,x=0,y=0):
        self._x = x
        self._y = y

    def add_dx(self,dx):
        self._x += dx
    def add_dy(self,dy):
        self._y += dy
    def copy(self):
        return Point(self._x,self._y)
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,x):
        self._x = x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,y):
        self._y = y
    @property
    def coordinate(self):
        return (self.x,self.y)
    @coordinate.setter
    def coordinate(self,coord):
        self.x,self.y = coord