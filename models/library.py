from models.book import Book
from models.user import User
from utils.file_manager import FileManager

class Library:
    def __init__(self):
        self.file_manager = FileManager()
        self.books = []
        self.users = []

    def load_data(self):
        self.books = [Book(**b) for b in self.file_manager.load_json('data/books.json')]
        self.users = [User(**u) for u in self.file_manager.load_json('data/users.json')]

    def save_data(self):
        self.file_manager.save_json('data/books.json', [b.__dict__ for b in self.books])
        self.file_manager.save_json('data/users.json', [u.__dict__ for u in self.users])

    def find_book(self, book_id):
        return next((b for b in self.books if b.book_id == book_id), None)

    def find_user(self, user_id):
        return next((u for u in self.users if u.user_id == user_id), None)

    def display_books(self):
        print("\n📚 Available Books:")
        for book in self.books:
            print(book)
