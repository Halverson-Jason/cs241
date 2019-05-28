# Checkpoint #6 A
# Jason Halverson

class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication = 0
    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication = int(input("Publication Year: "))
    def display_book_info(self):
        print("\n{title} ({publication}) by {author}".format(title = self.title,publication = self.publication, author = self.author))

class TextBook(Book):
    def __init__(self):
        self.subject = ""
        print()
    def prompt_subject(self):
        self.subject = input("Subject: ")
    def display_subject(self):
        print("Subject: {}\n".format(self.subject))

class PictureBook(Book):
    def __init__(self):
        self.illustrator = ""
    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")
    def display_illustrator(self):
        print("Illustrated by {}".format(self.illustrator))

def main():
    book = Book()
    book.prompt_book_info()
    book.display_book_info()

    textbook = TextBook()
    textbook.prompt_book_info()
    textbook.prompt_subject()
    textbook.display_book_info()
    textbook.display_subject()

    picturebook = PictureBook()
    picturebook.prompt_book_info()
    picturebook.prompt_illustrator()
    picturebook.display_book_info()
    picturebook.display_illustrator()

if __name__ == "__main__":
    main()