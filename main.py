from models.library import Library

def main():
    library = Library()
    library.load_data()

    print("\nWelcome to the 📖 Library Management System!")

    while True:
        print("\n===== MENU =====")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.display_books()

        elif choice == '2':
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            user = library.find_user(user_id)
            book = library.find_book(book_id)

            if user and book:
                user.borrow_book(book)
                library.save_data()
            else:
                print("❌ Invalid user or book ID.")

        elif choice == '3':
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            user = library.find_user(user_id)
            book = library.find_book(book_id)

            if user and book:
                user.return_book(book)
                library.save_data()
            else:
                print("❌ Invalid user or book ID.")

        elif choice == '4':
            print("Goodbye 👋")
            break

        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
