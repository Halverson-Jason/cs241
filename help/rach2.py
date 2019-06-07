from collections import deque

class Student:
    def __init__(self):
        self.name = ""
        self.course = ""

    def prompt(self):
        self.name = input("Enter name: ")
        self.course = input("Enter course: ")
        return(self.name, self.course)

    def display(self):
        print("Now helping {} with {}".format(self.name, self.course))

class HelpSystem:
    def __init__(self):
        self.waiting_list = deque()

    def is_student_waiting(self):
        if len(self.waiting_list) == 0:
            result = False
        else:
            result = True
        return result

    def add_to_waiting_list(self):
        new_student = Student()
        new_student.prompt()
        self.waiting_list.append(new_student)

    def help_next_student(self):
        currentStudent = self.waiting_list.popleft()
        currentStudent.display()

class main:
    h = HelpSystem()
    option = 0

    while option != 3:
        print()
        print("Options:")
        print("1. Add a new student")
        print("2. Help next student")
        print("3. Quit")
        option = int(input("Enter selection: "))
        print()
        if option == 1:
            h.add_to_waiting_list()
        elif option == 2:
            if h.is_student_waiting() == False:
                print("No one to help.")
            else:
                h.help_next_student()

    else:
        print("Goodbye")

if __name__ == "__main__":
    main()