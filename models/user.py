class User:
    def __init__(self, user_id, name, borrowed_books=None):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = borrowed_books or []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book.book_id)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is currently not available.")

    def return_book(self, book):
        if book.book_id in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.book_id)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} doesn’t have '{book.title}' borrowed.")

    def __str__(self):
        return f"User: {self.name}, Borrowed Books: {self.borrowed_books}"
