from pymongo import MongoClient

# Replace with your MongoDB Atlas connection string
client = MongoClient("mongodb+srv://admin:admin@instabase.svzbc.mongodb.net/?retryWrites=true&w=majority&appName=Instabase")

db = client["movie_db"]
movies_collection = db["movies"]

# Sample movie data
# sample_movies = [
#     {"title": "Inception", "director": "Christopher Nolan", "release_year": 2010, "runtime": 148, "genres": ["Action", "Sci-Fi"], "rating": 8.8},
#     {"title": "The Dark Knight", "director": "Christopher Nolan", "release_year": 2008, "runtime": 152, "genres": ["Action", "Crime"], "rating": 9.0},
#     {"title": "Interstellar", "director": "Christopher Nolan", "release_year": 2014, "runtime": 169, "genres": ["Adventure", "Drama"], "rating": 8.6},
#     {"title": "The Great Train Robbery", "director": "Edwin S. Porter", "release_year": 1903, "runtime": 12, "genres": ["Western", "Short"], "rating": 7.3},
#     {"title": "The Shawshank Redemption", "director": "Frank Darabont", "release_year": 1994, "runtime": 142, "genres": ["Drama"], "rating": 9.3},
#     {"title": "Pulp Fiction", "director": "Quentin Tarantino", "release_year": 1994, "runtime": 154, "genres": ["Crime", "Drama"], "rating": 8.9},
#     {"title": "The Godfather", "director": "Francis Ford Coppola", "release_year": 1972, "runtime": 175, "genres": ["Crime", "Drama"], "rating": 9.2},
#     {"title": "Fight Club", "director": "David Fincher", "release_year": 1999, "runtime": 139, "genres": ["Drama"], "rating": 8.8},
#     {"title": "Forrest Gump", "director": "Robert Zemeckis", "release_year": 1994, "runtime": 142, "genres": ["Drama", "Romance"], "rating": 8.8},
#     {"title": "The Matrix", "director": "Lana Wachowski", "release_year": 1999, "runtime": 136, "genres": ["Action", "Sci-Fi"], "rating": 8.7},
# ]

# movies_collection.insert_many(sample_movies)

query = {"release_year": { "$gt": 2000 }, "runtime": { "$gt": 120 }}
movies_collection.find(query)