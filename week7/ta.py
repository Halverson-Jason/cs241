from abc import ABC
from abc import abstractclassmethod

class Employee(ABC):
    def __init__(self):
        self.name = ""
    def prompt_name(self):
        self.name = input("Please enter your name: ")

    @abstractclassmethod
    def display(self):
        pass
    def prompt_wage(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hourly_wage = 0
    def display(self):
        print("{} - ${}/hour".format(self.name,self.hourly_wage))
    def prompt_wage(self):
        self.hourly_wage = input("Input your Hourly Wage: ")

class SalaryEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.salary = 0
    def display(self):
        print("{} - ${}/year".format(self.name,self.salary))
    def prompt_wage(self):
        self.salary = input("Input your Salary: ")

def main():
    employees = []
    user_input = input("Enter 'h' for hourly, 's' for salary or Enter 'q' to quit:")
    while user_input != 'q':
        if user_input == 's':
            e = SalaryEmployee()
            e.prompt_name()
            e.prompt_wage()
            employees.append(e)

        elif user_input == 'h':
            e = HourlyEmployee()
            e.prompt_name()
            e.prompt_wage()
            employees.append(e)

        user_input = input("Enter 'h' for hourly, 's' for salary or Enter 'q' to quit:")

    for employee in employees:
        employee.display()

if __name__ == "__main__":
    main()