class Book:
    def __init__(self, title, author, _id ):
        self.title = title
        self.author = author
        self._id = _id
        self.borrowed = False


    def getid(self):
        return self._id

    def gettitle(self):
        return self.title

    def getauthor(self):
        return  self.author

    def getbyid(self):
        return f"{self.gettitle()} - {self.getauthor()}"

    def get_borrowed(self):
        return self.borrowed

    def set_borrowed(self):
        if self.borrowed :
            self.borrowed = False
        else:
            self.borrowed = True

    def __str__(self):
        return f"Book : {self._id} - {self.title} - {self.author} - {self.borrowed}"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrow = []

    def getid(self):
        return self.user_id

    def getname(self):
        return self.name

    def get_books_borrowed(self):
        return self.books_borrow

    def display_user(self):
        l = ", ".join(self.books_borrow) if self.books_borrow else "empty"
        return f"User : {self.user_id} - {self.name} - [{l}]"

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def register_book(self, book):
        if book.getid() in self.books:
            print("already there is a book")
        else:
            self.books[book.getid()] = book
        return "book registered"

    def register_user(self, user):
        if user.getid() in self.users:
            return "user already registered"
        self.users[user.getid()] = user
        return "user registered"

    def borrow_book(self, user, book):
        books = user.get_books_borrowed()
        if book.getid() in books:
            return "already borrowed"
        books.append(book.getid())
        book.set_borrowed()
        return "book borrowed"

    def return_book(self, user, book):
        books = user.get_books_borrowed()
        if book.getid() not in books:
            return "book not borrowed"
        books.remove(book.getid())
        book.set_borrowed()
        return "book returned"

    def display(self):
        print("---------available books----------")
        if not self.books:
            print("no books available")
            return
        else:
            for i in self.books.values():
                print(f"{i.getid()} - {i.gettitle()} - {i.getauthor()} - {i.get_borrowed()}")
            print("----------------------------------")
        print("---------available Users----------")
        if not self.users:
            print("no users available")
            return
        else:
            for i in self.users.values():
                print(f"{i.getid()} - {i.getname()} - {i.get_books_borrowed()}")
            print("----------------------------------")



print("-------welcome------")
lib = Library()
while True:
    print("1.add book\n"
          "2.add user\n")
    n = int(input("enter the choice: "))
    if n == 1:
        title = input("enter the title: ")
        author = input("enter the author: ")
        id = input("enter the id: ")
        lib.register_book(Book(title, author, id))
        lib.display()

    elif n == 2:
        id = input("enter the id: ")
        name = input("enter the name: ")
        lib.register_user(User(id, name))
        lib.display()
    else:
        break




# # print("\nBooks ->")
# b_oop = Book("Python OOP Masterclass", "Smith", "978-12345",)
# # print(b_oop)
# b_data = Book("The Data Handbook", "Jones", "978-67890")
# # print(b_data, end="\n\n")
# # r_history = ReferenceBook("World Atlas of History", "Clark", "978-00001", "Geography")
# # print("Users ->")
# u_alice = User("U101", "Alice Johnson")
# # print(u_alice.display_user())
# u_bob = User("U102", "Bob Williams")
# # print(u_bob.display_user(), "\n")
#
# lib = Library()
# lib.register_book(b_oop)
# lib.register_book(b_data)
# lib.display()
#
# print(lib.borrow_book(u_bob, b_oop))
# # print(u_bob.display_user())
# print(lib.borrow_book(u_bob, b_data))
# # print(u_bob.display_user())
# #
# # lib.borrow_book(u_alice, b_data)
# # print(u_alice.display_user())
#
# lib.display()
# print(lib.return_book(u_bob, b_data))
# lib.display()
# # print(u_bob.display_user())
#
#
#
