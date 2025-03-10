from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os
from bson.objectid import ObjectId

#app = Flask(__name__)
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# MongoDB connection setup
# For Local MongoDB
# mongo_uri = "mongodb://localhost:27017/"

# For MongoDB Atlas
mongo_uri = "mongodb+srv://dbuser:dbUserPassword@flask.zvkal.mongodb.net/?retryWrites=true&w=majority&appName=flask"

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client['user_database']  # Database name
users_collection = db['users']  # Collection name


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        # Insert data into MongoDB
        user_data = {
            'name': data.get('name'),
            'email': data.get('email'),
            'message': data.get('message')
        }
        users_collection.insert_one(user_data)

        return jsonify({'message': 'Data submitted successfully!'})
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500


if __name__ == '_main_':
    app.run(debug=True)
