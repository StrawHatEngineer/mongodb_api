from flask import Flask, request, jsonify
from pymongo import MongoClient
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# MongoDB client connection
client = MongoClient("mongodb+srv://admin:admin@instabase.svzbc.mongodb.net/?retryWrites=true&w=majority&appName=Instabase")

@app.route('/query', methods=['POST'])
def query_movies():
    try:
        # Parse incoming JSON data
        data = request.get_json()
        db_name = data.get('db')
        query_type = data.get('query_type')  
        query = data.get('query') 
        limit = data.get('limit', 0)  
        collection_name = data.get('collection', None)

        db = client[db_name]
        
         # Handle listing of collections
        if query_type == 'listCollections':
            collection_names = db.list_collection_names()
            return jsonify({"collections": collection_names}), 200
        
        
        # Dynamic handling across collections if not specified
        if not collection_name:
            results = []
            collection_names = db.list_collection_names()
            for coll in collection_names:
                collection = db[coll]
                if query_type == 'find':
                    result = list(collection.find(query, {"_id": 0}).limit(limit)) if limit > 0 else list(collection.find(query, {"_id": 0}))
                elif query_type == 'aggregate':
                    temp_query = query[:]
                    if limit > 0:
                        temp_query.append({"$limit": limit})
                    result = list(collection.aggregate(temp_query))
                else:
                    return jsonify({"error": "Invalid query type. Use 'find' or 'aggregate'."}), 400

                if result:
                    results.append({ "collection": coll, "data": result })
            return jsonify(results), 200
        
        # Query specific collection
        collection = db[collection_name]

        if query_type == 'find':
            query_result = list(collection.find(query, {"_id": 0}).limit(limit)) if limit > 0 else list(collection.find(query, {"_id": 0}))
            return jsonify(query_result), 200

        elif query_type == 'aggregate':
            if limit > 0:
                query.append({"$limit": limit})
            query_result = list(collection.aggregate(query))
            return jsonify(query_result), 200

        else:
            return jsonify({"error": "Invalid query type. Use 'find' or 'aggregate'."}), 400

    except Exception as e:
        # Log error details
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
