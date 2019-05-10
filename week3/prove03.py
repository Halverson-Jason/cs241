class Robot:

    INITIAL_FUEL = 100
    INITIAL_COORD = 10
    DECREASE_FUEL_FIRE = 15
    DECREASE_FUEL_MOVE = 5

    def __init__(self):
        self.set_fuel_level(self.INITIAL_FUEL)
        self._location = {"xcoordinate":self.INITIAL_COORD, "ycoordinate":self.INITIAL_COORD}

    def fire(self):
        if self.check_fuel(self.DECREASE_FUEL_FIRE):
            print("Pew! Pew!")
            self.decrease_fuel_level(-self.DECREASE_FUEL_FIRE)

    def display(self):
        print("({}, {}) - Fuel: {}".format(self._location["xcoordinate"],self._location["ycoordinate"], self._fuel))

    def move(self, xcoord, ycoord):
        if self.check_fuel(self.DECREASE_FUEL_MOVE):
            self.set_xcoordinate(xcoord)
            self.set_ycoordinate(ycoord)
            self.decrease_fuel_level(-self.DECREASE_FUEL_MOVE)

    def set_xcoordinate(self,coordinate):
        self._location["xcoordinate"] = self._location["xcoordinate"] + coordinate

    def set_ycoordinate(self,coordinate):
        self._location["ycoordinate"] = self._location["ycoordinate"] + coordinate

    def set_fuel_level(self, level):
        self._fuel = level

    def decrease_fuel_level(self, decrease_amount):
        self._fuel = self._fuel + decrease_amount

    def check_fuel(self, decrease):
        if self._fuel >= decrease:
            return True
        else:
            print("Insufficient fuel to perform action")
            return False

def prompt_command():
	return input("Enter command: ").upper()


def play_game():
    """returns true if use wants to play again"""
    robot = Robot()
    input_correct = True
    while(input_correct):
        user_command = prompt_command()
        if user_command == "LEFT":
            robot.move(-1,0)
        elif user_command == "RIGHT":
            robot.move(1,0)
        elif user_command == "UP":
            robot.move(0,-1)
        elif user_command == "DOWN":
            robot.move(0,1)
        elif user_command == "FIRE":
            robot.fire()
        elif user_command == "STATUS":
            robot.display()
        elif user_command == "QUIT":
            return False

def main():
	play = True
	while(play):
		play = play_game()
	print("Goodbye.")
if __name__ == "__main__":
	main()