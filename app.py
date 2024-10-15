from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:admin@instabase.svzbc.mongodb.net/?retryWrites=true&w=majority&appName=Instabase")

@app.route('/query', methods=['POST'])
def query_movies():
    try:
        data = request.get_json()

        db = client[data.get('db', "demo_db")]
        query_type = data.get('type of query', 'find')  
        query = data.get('query', {}) 
        limit = data.get('limit', 0)  

        if query_type == 'listCollections':
            collection_names = db.list_collection_names()
            return jsonify({"collections": collection_names}), 200

        collection_name = data.get('collection', None)
        
        # go through all 
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


        collection = db[collection_name]

        if 'find' in query_type:
            if limit > 0:
                query_result = list(collection.find(query, {"_id": 0}).limit(limit))
            else:
                query_result = list(collection.find(query, {"_id": 0}))
            return jsonify(query_result), 200 
        elif query_type == 'aggregate':
            if limit > 0:
                query.append({"$limit": limit})  
            query_result = list(collection.aggregate(query))
            return jsonify(query_result), 200 
        else:
            return jsonify({"error": "Invalid query type. Use 'find' or 'aggregate'."}), 400 

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)