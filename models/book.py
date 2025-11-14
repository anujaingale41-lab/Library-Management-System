class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self._available = available  # private variable

    @property
    def available(self):
        return self._available

    def borrow(self):
        if self._available:
            self._available = False
            return True
        return False

    def return_book(self):
        self._available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"[{self.book_id}] {self.title} by {self.author} — {status}"
    