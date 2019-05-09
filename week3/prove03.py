class Robot:
    """
    Public:
        Methods:
            +fire()
            +display()
            +move(direction)
    Private:
        Methods:
            -get_x-coordinate()
            -set_x-coordinate()
            -get_y-coordinate()
            -set_y-coordinate()
            -get_fuel_level()
            -set_fuel_level()
    Variables:
        -x-coordinate
        -y-coordinate
        -fuel_level
    """
    INITIAL_FUEL = 100
    INITIAL_COORD = 10
    DECREASE_FUEL = 15
    def __init__(self):
        set_fuel_level(INITIAL_FUEL)
        _location = {"x-coordinate":INITIAL_COORD, "y-coordinate":INITIAL_COORD}

    def fire():
        print("Pew! Pew!")
        set_fuel_level()

    def display(self):
        print("({}, {}) - Fuel: {}".format(self._location["x-coordinate"],self._location["y-coordinate"], self._fuel))
#TODO: FINISH THE MOVE METHOD
    def move(direction):
        set_x-coordinate(direction)

    def set_x-coordinate(self,coordinate):
        self._location["x-coordinate"] = coordinate

    def set_y-coordinate(self,coordinate):
        self._location["y-coordinate"] = coordinate

    def set_fuel_level(self, level=None):
        """This is overloaded to either set the fuel level or decrease it if called"""
        if level is not None:
            self._fuel = level
        else:
            self._fuel = self._fuel - DECREASE_FUEL
#TODO: Create main class and game logic