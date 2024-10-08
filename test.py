from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your MongoDB Atlas connection details
MONGODB_URI = "https://data.mongodb-api.com/app/data-cibzeymf/endpoint/data/v1/"
API_KEY = "5b37c2ae-c9e3-4315-8555-c514bd31a425"  # Replace with your actual API key

@app.route('/query', methods=['POST'])
def query_movies():
    try:
        data = request.get_json()
        
        # Construct the request to MongoDB Atlas API
        db_name = data.get('db')
        collection_name = data.get('collection')
        query = data.get('query')

        url = f"{MONGODB_URI}action/findOne"
        headers = {
            "Content-Type": "application/json",
            "api-key": API_KEY,
        }

        payload = {
            "dataSource": "instabase",  # Replace with your data source name
            "database": db_name,
            "collection": collection_name,
            "filter": query,
            "projection": {"_id": 0}  # Exclude the _id field from the result
        }

        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": response.json()}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
