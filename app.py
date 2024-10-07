from app import Flask, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:admin@instabase.svzbc.mongodb.net/?retryWrites=true&w=majority&appName=Instabase")
db = client["movie_db"]
movies_collection = db["movies"]

@app.route('/query', methods=['POST'])
def query_movies():
    data = request.get_json()

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
