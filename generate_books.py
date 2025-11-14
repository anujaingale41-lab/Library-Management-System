import json
import random

# Some sample words to generate titles and authors
adjectives = [
    "Silent", "Hidden", "Brave", "Lost", "Dark", "Golden", "Fading", "Burning",
    "Frozen", "Endless", "Wandering", "Crimson", "Secret", "Infinite"
]
nouns = [
    "Dreams", "Voices", "Empire", "Journey", "Forest", "Sky", "Legacy", "Ocean",
    "World", "Horizon", "Path", "Memory", "Fire", "Destiny"
]
first_names = [
    "James", "Sophia", "Liam", "Emma", "Olivia", "Noah", "Ava", "Ethan", "Mia",
    "Lucas", "Isabella", "Mason", "Amelia", "Elijah", "Charlotte", "Harper"
]
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Taylor", "Anderson", "Davis",
    "Wilson", "Thomas", "Moore", "Martin", "Lee", "Clark", "Walker", "Hall"
]

# Generate 100 random books
books = []
for i in range(1, 101):
    title = f"The {random.choice(adjectives)} {random.choice(nouns)}"
    author = f"{random.choice(first_names)} {random.choice(last_names)}"
    book = {
        "book_id": f"B{i:03}",
        "title": title,
        "author": author,
        "available": True
    }
    books.append(book)

# Save to JSON file
with open("data/books.json", "w") as f:
    json.dump(books, f, indent=4)

print("✅ Successfully generated 100 books in data/books.json")
