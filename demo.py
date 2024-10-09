import random
from pymongo import MongoClient
from faker import Faker

# Create a Faker instance to generate random data
fake = Faker()

# MongoDB connection
client = MongoClient("mongodb+srv://admin:admin@instabase.svzbc.mongodb.net/?retryWrites=true&w=majority&appName=Instabase")
db = client['library_db']
books_collection = db['books']

# Generate and insert 9000 book documents
for _ in range(9000):
    book = {
        "title": fake.sentence(nb_words=random.randint(2, 5)),  # Random title
        "author_id": random.randint(1, 1000),  # Assuming you have 1000 authors
        "published_year": random.randint(1900, 2024),  # Random year between 1900 and 2024
        "pages": random.randint(50, 1000),  # Random page count between 50 and 1000
        "genre": random.choice(['Fiction', 'Non-Fiction', 'Science', 'Fantasy', 'Mystery', 'Biography', 'Thriller'])  # Random genre
    }
    
    books_collection.insert_one(book)

print("Successfully added 9000 documents to the books collection.")
