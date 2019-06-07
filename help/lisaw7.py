class Book():
   def __init__(self):
       # Define member variables to be shared by derived classes
       self.title = ""
       self.author = ""
       self.publication_year = 0

   def prompt_book_info(self):
       self.title = (input("Title: "))
       self.author = (input("Author: "))
       self.publication_year = (input("Publication Year: "))

   def display_book_info(self):
       print("{} ({}) by {}" .format(self.title, self.publication_year, self.author))

#Put Book into the parentheses to show the class is inheriting
class Textbook(Book):
   def __init__(self):
       # Override the base class __init__ function by using super().__init__
       # to ensure that the member variables in the base class also get set up.
       # First call the base class version
       super().__init__()
       # Now, set up any member variables
       self.subject = ""

   def prompt_subject(self):
       self.prompt_book_info()
       self.subject = (input("Subject: "))

   def display_subject(self):
       super().display_book_info()
       print("{}" .format(self.subject))

class PictureBook(Book):
   def __init__(self):
       super().__init__()
       self.illustrator = ""

   def prompt_illustrator(self):
       self.prompt_book_info()
       self.illustrator = (input("Illustrator: "))

   def display_illustrator(self):
       super().display_book_info()
       print("{}" .format(self.illustrator))

def main():
   b = Book()
   b.prompt_book_info()
   b.display_book_info()

   print()

   t = TextBook()
   t.prompt_book_info()
   t.prompt_subject()
   t.display_book_info()
   t.display_subject()

   print()

   p = PictureBook(Book)
   p.prompt_book_info()
   p.prompt_illustrator()
   p.display_book_info()
   p.display_illustrator()

if __name__ == "__main__":
   main()