from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:admin@instabase.svzbc.mongodb.net/?retryWrites=true&w=majority&appName=Instabase")


@app.route('/query', methods=['POST'])
def query_movies():
    try:
        
        data = request.get_json()
        db = data.get('db')
        collection_name = data.get('collection')
        queries = data.get('queries', []) 

        collection = db[collection_name]
        results = []

        for query in queries:
            query_results = list(collection.find(query, {"_id": 0}))  
            results.append(query_results)  

        return jsonify(results), 200 

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
