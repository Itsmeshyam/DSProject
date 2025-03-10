from datetime import datetime
from flask import Flask, request, jsonify, render_template, url_for
from pymongo import MongoClient
import os

app = Flask(__name__ , template_folder='../frontend/templates', static_folder='../frontend/static')

# MongoDB connection URI
mongo_uri = "mongodb+srv://dbUser:dbUserPassword@flask.rcv6r.mongodb.net/?retryWrites=true&w=majority&appName=flask"

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client.get_database('student_health_card')  # Replace with your database name
users_collection = db.users  # Replace with your collection name

# Routes
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/benefits')
def benefits():
    return render_template('benefits.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        # Validate required fields
        if not data.get('name') or not data.get('email') or not data.get('phone'):
            return jsonify({'message': 'Name, email, and phone are required'}), 400

        # Convert date string to a Python date object
        dob_str = data.get('dob')
        dob = None
        if dob_str:
            try:
                dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'message': 'Invalid date format. Use YYYY-MM-DD.'}), 400

        # Create a new user document
        new_user = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
            'dob': dob.isoformat(),
            'street': data.get('street'),
            'city': data.get('city'),
            'state': data.get('state'),
            'postal': data.get('postal'),
            'country': data.get('country'),
            'institution': data.get('institution'),
            'student_id': data.get('student-id'),
            'message': data.get('message')
        }

        # Insert the new user into the MongoDB collection
        users_collection.insert_one(new_user)

        # Return a success response with a redirect URL
        return jsonify({
            'message': 'Data submitted successfully!',
            'redirect': url_for('thank_you')  # URL for the Thank You page
        })
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500


@app.route('/thank-you')
def thank_you():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)