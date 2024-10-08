from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:admin@instabase.svzbc.mongodb.net/?retryWrites=true&w=majority&appName=Instabase")

@app.route('/query', methods=['POST'])
def query_movies():
    try:
        data = request.get_json()

        db = client[data.get('db')]
        collection_name = data.get('collection')
        query_type = data.get('type of query')  # Added query_type
        query = data.get('query') 

        collection = db[collection_name]

        if query_type == 'find':
            # Execute a find query
            query_result = list(collection.find(query, {"_id": 0}))  
            return jsonify(query_result), 200 

        elif query_type == 'aggregate':
            # Execute an aggregate query
            query_result = list(collection.aggregate(query))  # No need to filter out _id here
            return jsonify(query_result), 200 

        else:
            return jsonify({"error": "Invalid query type. Use 'find' or 'aggregate'."}), 400 

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
