class Point:
    def __init__(self):
        self._x = 0
        self._y = 0

    def add_dx(self,dx):
        self._x += dx
    def add_dy(self,dy):
        self._y += dy

    @property
    def center_x(self):
        return self._x
    @center_x.setter
    def center_x(self,x):
        self._x = x

    @property
    def center_y(self):
        return self._y
    @center_y.setter
    def center_y(self,y):
        self._y = y