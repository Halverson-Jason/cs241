from abc import ABC
from abc import abstractmethod

class Shape(ABC):
    def __init__(self):
        self.name = ""
        super().__init__()
        self.radius = 0.0
        self.length = 0.0
        self.width = 0.0

    @abstractmethod
    def get_area(self):
        return area
    
    def display(self):
        print("{} - {:.2f}".format(self.name, area))

class Circle(Shape):
   
    def __init__(self, radius):
        super().__init__()
        self.name = "circle"
        self.radius = radius
        
    def get_area(self):
        return float(3.14 * self.radius * self.radius)
    
#    def display(self):
#        self.area = get_area(radius)
#        view = print("{} - {:.2f}".format(self.name, self.area))
#        return view

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.name = 'Rectangle'
        self.length = length
        self.width = width
        
    def get_area(self, length, width):
        return float(self.length * self.width)
    
#    def display(self):
#        display = print("{} - {:.2f}".format(self.name, self.area))
#        return display
    
def main():

    shapes = []
    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            c = Circle(radius)
            shapes.append(c)

        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            r = Rectangle(length, width)
            shapes.append(r)
            
    #TODO: Loop through each shape in the list, and call its display function
    print(shapes)
    for shape in shapes:
        shape.display()
        
if __name__ == "__main__":
    main()