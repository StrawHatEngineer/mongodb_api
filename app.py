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
        query = data.get('query') 

        collection = db[collection_name]
        result = []

        query_result = list(collection.find(query, {"_id": 0}))  
        result.append(query_result)  

        return jsonify(result), 200 

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
