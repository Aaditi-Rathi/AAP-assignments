class Book:
    def __init__(self, title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_borrowed=False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed=True
            print(f"{self.title} has been borrowed")
        else:
            print(f"{self.title}  is not available.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print(f"{self.title} has been returned")
        else:
            print(f"{self.title} was never borrowed.")

class Patron:
    def __init__(self, name, patron_id):
        self.name=name
        self.patron_id=patron_id
        self.borrowed_book=[]

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_book.append(book)

        else:
            print(f"{book.title} is unavailable")

    def return_book(self, book):
            if book in self.borrowed_book:
                book.return_book()
                self.borrowed_book.remove(book)
            else:
                print(f"{self.name} did not borrow {book.title}. ")

class Library:
    def __init__(self):
        self.book=[]
        self.patron=[]

    def add_books(self, book):
        self.book.append(book)
        print(f"Book {book.title} added")
       
    def register_patron(self, patron):
        self.patron.append(patron)
        print(f"Patron {patron.name} registered.")

    def borrow_book(self,patron, book):
        patron.borrow_book(book)
    def return_book(self,patron,book):
        patron.return_book(book)

library=Library()
book1= Book("Pride and Prejudice","Jane Austen","101")
book2= Book("The Alchemist","Paulo Coelho","11")

library.add_books(book1)
library.add_books(book2)

patron1=Patron("Pranjali","abc12")
patron2=Patron("Ishu","23xyz")

library.register_patron(patron1)
library.register_patron(patron2)

library.borrow_book(patron1,book1)
library.borrow_book(patron2,book2)

library.return_book(patron1,book1)
library.return_book(patron2,book2)