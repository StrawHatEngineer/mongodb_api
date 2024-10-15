from pymongo import MongoClient
import random
import string

# Connect to MongoDB
client = MongoClient("mongodb+srv://admin:admin@instabase.svzbc.mongodb.net/?retryWrites=true&w=majority&appName=Instabase")

# Specify the database name
db_name = "demo_db"
db = client[db_name]

# Sample data for employees and movies
first_names = ["John", "Jane", "Alice", "Bob", "Chris", "Emily", "David", "Laura", "Michael", "Sarah"]
last_names = ["Smith", "Doe", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Taylor"]
email_domains = ["example.com", "sample.com", "test.com", "demo.com"]
movie_titles = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", 
                "The Lord of the Rings", "Forrest Gump", "Inception", "The Matrix", 
                "Fight Club", "The Empire Strikes Back"]

# Function to generate random employee data
def generate_random_employee():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(email_domains)}"
    return {
        "name": f"{first_name} {last_name}",
        "age": random.randint(18, 65),
        "address": generate_random_string(15),  # Random address for now
        "email": email,
        "phone": ''.join(random.choices(string.digits, k=10)),
        "active": random.choice([True, False])
    }

# Function to generate random movie data
def generate_random_movie():
    return {
        "title": random.choice(movie_titles),
        "release_year": random.randint(1980, 2023),
        "genre": random.choice(["Action", "Drama", "Comedy", "Horror", "Thriller", "Sci-Fi", "Fantasy"]),
        "director": generate_random_string(10),  # Random director name for now
        "rating": round(random.uniform(1.0, 10.0), 1)
    }

# Function to generate random string data for addresses and director names
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Number of collections and documents
num_collections = 500  # Set to a smaller number for demonstration
documents_per_collection = 10000  # Set to a smaller number for demonstration

# Loop to create collections and insert documents
for i in range(num_collections):
    collection_name = f"employees_{i+1}"  # Collection for employees
    collection = db[collection_name]
    
    # Generate a list of documents for employees
    employee_documents = [generate_random_employee() for _ in range(documents_per_collection)]
    
    # Insert documents into the collection
    collection.insert_many(employee_documents)
    
    print(f"Inserted {documents_per_collection} employee documents into {collection_name}")

    # Create another collection for movies
    collection_name = f"movies_{i+1}"  # Collection for movies
    collection = db[collection_name]
    
    # Generate a list of documents for movies
    movie_documents = [generate_random_movie() for _ in range(documents_per_collection)]
    
    # Insert documents into the collection
    collection.insert_many(movie_documents)
    
    print(f"Inserted {documents_per_collection} movie documents into {collection_name}")

print("Data insertion completed!")
