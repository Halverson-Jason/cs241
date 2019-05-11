class Person:

    def __init__(self, name=None, birth_year=None):
        if name == None:
            self.name = "anonymous"
        else:
            self.name = name
        if birth_year == None:
            self.birth_year = "unknown"
        else:
            self.birth_year = birth_year

    def display(self):
        print("{} (b. {})".format(self.name, self.birth_year))

class Book:
    def __init__(self, title=None, author=None, publisher=None):
        if title == None:
            self.title = "untitled"
        else:
            self.title = title
        if author == None:
            self.author = Person()
        else:
            self.author = author
        if publisher == None:
            self.publisher = "unpublished"
        else:
            self.publisher = publisher
    def display(self):
        print("{}".format(self.title))
        print("Publisher:\n{}".format(self.publisher))
        print("Author:")
        self.author.display()


def initial_prompt_message():
    print("\nPlease enter the following:")

def prompt_author():
    # set prompt author, set author
    author_name = input("Name: ")
    author_birth_year = input("Year: ")
    author = Person(author_name,author_birth_year)
    return  author

def prompt_title():
    return input("Title: ")
def prompt_publisher():
    # set prompt author, set author
    return input("Publisher: ")

def main():
    # initial display
    book = Book()
    book.display()

    # get user input
    initial_prompt_message()
    author = prompt_author()
    title = prompt_title()
    publisher = prompt_publisher()
    print()
    book2 = Book(title,author,publisher)
    book = book2

    # final display
    book.display()

if __name__ == "__main__":
    main()