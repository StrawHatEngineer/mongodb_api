from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection string (consider moving to environment variables for security)
MONGODB_URI = "mongodb+srv://admin:admin@instabase.svzbc.mongodb.net/?retryWrites=true&w=majority&appName=Instabase"
client = MongoClient(MONGODB_URI)

@app.route('/query', methods=['POST'])
def query_movies():
    data = request.get_json()

    # Retrieve database and collection names from the request
    db_name = data.get("db")
    collection_name = data.get("collection")

    if not db_name or not collection_name:
        return jsonify({"error": "Please provide both 'db' and 'collection'."}), 400

    # Access the specified database and collection
    db = client[db_name]
    movies_collection = db[collection_name]

    # Example prompt processing (this can be improved with LLM)
    prompt = data.get("prompt", "")

    # Map user prompts to MongoDB queries (simple example)
    if "find all movies directed by" in prompt.lower():
        director_name = prompt.split("directed by")[-1].strip().strip(".")
        results = list(movies_collection.find({"director": director_name}, {"_id": 0}))

    elif "find all movies released after" in prompt.lower():
        year = int(prompt.split("after")[-1].strip().strip("."))
        results = list(movies_collection.find({"release_year": {"$gt": year}}, {"_id": 0}))

    elif "find all movies with rating above" in prompt.lower():
        rating = float(prompt.split("above")[-1].strip().strip("."))
        results = list(movies_collection.find({"rating": {"$gt": rating}}, {"_id": 0}))

    else:
        return jsonify({"error": "Invalid query prompt."}), 400

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
