## 1. Book Class (Encapsulation)
class Book:
    """Represents a book in the library."""
    def __init__(self, title, author, isbn):
        # Protected attributes (conventionally denoted by a single underscore)
        self._title = title
        self._author = author
        self._isbn = isbn
        self._is_borrowed = False  # Encapsulated state

    def get_isbn(self):
        """Getter for ISBN, useful for library lookups."""
        return self._isbn

    def get_title(self):
        """Getter for Title."""
        return self._title

    def is_available(self):
        """Checks the borrowing status."""
        return not self._is_borrowed

    def borrow(self):
        """Attempts to borrow the book."""
        if not self._is_borrowed:
            self._is_borrowed = True
            return f"✅ '{self._title}' has been successfully borrowed."
        return f"❌ '{self._title}' is already borrowed."

    def return_book(self):
        """Attempts to return the book."""
        if self._is_borrowed:
            self._is_borrowed = False
            return f"✅ '{self._title}' has been successfully returned."
        return f"❌ '{self._title}' was not checked out."

    def __str__(self):
        """String representation of the book."""
        status = "Available" if not self._is_borrowed else "Borrowed"
        return f"Book: {self._title} by {self._author} (ISBN: {self._isbn}) - Status: {status}"

# ----------------------------------------------------------------------

## 2. Specialized Book Class (Inheritance & Polymorphism)
class ReferenceBook(Book):
    """Represents a book that cannot be borrowed (must stay in the library)."""
    def __init__(self, title, author, isbn, subject):
        super().__init__(title, author, isbn)
        self._subject = subject

    # Polymorphism: Overriding the parent's method
    def borrow(self):
        """Reference books cannot be checked out."""
        return f"🛑 '{self._title}' is a **Reference Book** and must be read within the library."

    def __str__(self):
        """Updated string representation."""
        return f"Reference Book: {self._title} ({self._subject}) by {self._author} (ISBN: {self._isbn})"

# ----------------------------------------------------------------------

## 3. User Class
class User:
    """Represents a library user."""
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        # Stores Book objects
        self._borrowed_books = []

    def get_id(self):
        """Getter for User ID."""
        return self._user_id

    def get_name(self):
        """Getter for Name."""
        return self._name

    def borrow_book(self, book):
        """Adds a book object to the user's borrowed list."""
        self._borrowed_books.append(book)

    def return_book(self, book):
        """Removes a book object from the user's borrowed list."""
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            return True
        return False

    def list_borrowed(self):
        """Returns a list of titles the user has checked out."""
        if not self._borrowed_books:
            return "No books currently borrowed."

        titles = [b.get_title() for b in self._borrowed_books]
        return f"📚 Books borrowed by {self._name}: {', '.join(titles)}"

    def __str__(self):
        return f"User: {self._name} (ID: {self._user_id})"

# ----------------------------------------------------------------------

## 4. Library Class (Composition)
class Library:
    """Manages the collection of books and registered users."""
    def __init__(self):
        # Composition: Library 'has-a' collection of books and users
        # Key: ISBN, Value: Book object
        self._books = {}
        # Key: user_id, Value: User object
        self._users = {}

    def add_book(self, book):
        """Adds a book or reference book to the collection."""
        if book.get_isbn() in self._books:
            return f"❌ Book with ISBN {book.get_isbn()} already exists."
        self._books[book.get_isbn()] = book
        print(f"➕ Added book: {book.get_title()}")

    def register_user(self, user):
        """Registers a user."""
        if user.get_id() in self._users:
            return f"❌ User with ID {user.get_id()} is already registered."
        self._users[user.get_id()] = user
        print(f"👤 Registered user: {user.get_name()}")

    def checkout_book(self, user_id, isbn):
        """Handles the book checkout process."""
        if user_id not in self._users:
            return "❌ Error: User not found."
        if isbn not in self._books:
            return "❌ Error: Book not found in library inventory."

        user = self._users[user_id]
        book = self._books[isbn]

        # 1. Attempt to borrow the book (handles availability and ReferenceBook polymorphism)
        borrow_result = book.borrow()

        # 2. Check if the book's state was actually updated (i.e., not a 'ReferenceBook' fail or already borrowed fail)
        if "successfully borrowed" in borrow_result:
            user.borrow_book(book)
            print(f"--- Checkout Successful ---")
            print(f"User: {user.get_name()} checked out: {book.get_title()}")

        return borrow_result

    def return_book(self, user_id, isbn):
        """Handles the book return process."""
        if user_id not in self._users:
            return "❌ Error: User not found."
        if isbn not in self._books:
            return "❌ Error: Book not found in library inventory."

        user = self._users[user_id]
        book = self._books[isbn]

        # 1. Check if the user had the book
        if user.return_book(book):
            # 2. Update the book's status
            return_result = book.return_book()
            print(f"--- Return Successful ---")
            print(f"User: {user.get_name()} returned: {book.get_title()}")
            return return_result
        else:
            return f"❌ Error: {user.get_name()} did not borrow the book with ISBN {isbn}."

    def display_all_books(self):
        """Prints the status of all books."""
        print("\n--- Current Library Inventory ---")
        if not self._books:
            print("The library is empty.")
            return

        for book in self._books.values():
            print(book)
        print("---------------------------------")

# ----------------------------------------------------------------------
## 🚀 Driver Code / Testing the System
# ----------------------------------------------------------------------

# 1. Setup Library
main_library = Library()

# 2. Create Books (Demonstrating Inheritance)
b_oop = Book("Python OOP Masterclass", "Smith", "978-12345",)
print(b_oop)
b_data = Book("The Data Handbook", "Jones", "978-67890")
r_history = ReferenceBook("World Atlas of History", "Clark", "978-00001", "Geography")

# 3. Create Users
u_alice = User("U101", "Alice Johnson")
u_bob = User("U102", "Bob Williams")

# 4. Add to Library
main_library.add_book(b_oop)
main_library.add_book(b_data)
main_library.add_book(r_history)
main_library.register_user(u_alice)
main_library.register_user(u_bob)

main_library.display_all_books()

# 5. Test Checkout and Encapsulation
print("\n=== Testing Checkout ===")
print(main_library.checkout_book(u_alice.get_id(), b_oop.get_isbn())) # Alice checks out OOP book
print(u_alice.list_borrowed())

print("\n--- Test 1: Borrowing an already borrowed book ---")
print(main_library.checkout_book(u_bob.get_id(), b_oop.get_isbn())) # Bob tries to checkout the same book
print(u_bob.list_borrowed())

print("\n--- Test 2: Reference Book Polymorphism ---")
print(main_library.checkout_book(u_bob.get_id(), r_history.get_isbn())) # Bob tries to checkout a reference book
print(r_history) # Status should still be 'Available' due to no state change

# 6. Test Return
print("\n=== Testing Return ===")
print(main_library.return_book(u_alice.get_id(), b_oop.get_isbn())) # Alice returns the OOP book
print(u_alice.list_borrowed())

main_library.display_all_books()