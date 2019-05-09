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
    DECREASE_FUEL_FIRE = 15
	DECREASE_FUEL_MOVE = 5
	
    def __init__(self):
        set_fuel_level(INITIAL_FUEL)
        _location = {"x-coordinate":INITIAL_COORD, "y-coordinate":INITIAL_COORD}

    def fire():
        print("Pew! Pew!")
        decrease_fuel_level(DECREASE_FUEL_FIRE)

    def display(self):
        print("({}, {}) - Fuel: {}".format(self._location["x-coordinate"],self._location["y-coordinate"], self._fuel))

    def move(x-coord,y-coord):
        set_x-coordinate(x-coord)
		set_y-coordinate(y-coord)
		decrease_fuel_level(DECREASE_FUEL_MOVE)

    def set_x-coordinate(self,coordinate):
        self._location["x-coordinate"] = coordinate

    def set_y-coordinate(self,coordinate):
        self._location["y-coordinate"] = coordinate

    def set_fuel_level(self, level):
        self._fuel = level
		
	def decrease_fuel_level(self, decrease_amount):
		self._fuel = self._fuel + decrease_amount
	def insufficient_fuel():
		print()

def prompt_command():
	return input("Enter command: ")
	
#TODO: Create main class and game logic
def play_game()
	"""returns true if use wants to play again"""
	robot = Robot()
	user_command = prompt_command()
	while(input_correct):
		switch(user_command):
			case "LEFT":
				robot.move(-1,0)
			case "RIGHT":
				robot.move(1,0)
			case "UP":
				robot.move(0,-1)
			case "DOWN":
				robot.move(0,1)
			case "FIRE":
				robot.fire()
			case "STATUS":
				robot.display()
			case "QUIT":
				return false
			default:
				print("")
				input_correct = False
		
	
	
	
def main():
	play = True
	while(play):
		play = play_game()	
	print("Goodbye")
if __init__ == "__main__":
	main()