from datetime import datetime, date
from flask import Flask, request, jsonify, render_template, url_for
from pymongo import MongoClient
import re
import phonenumbers
import pycountry

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# MongoDB connection URI
mongo_uri = "mongodb+srv://dbUser:dbUserPassword@flask.rcv6r.mongodb.net/?retryWrites=true&w=majority&appName=flask"

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client.get_database('student_health_card')
users_collection = db.users  # Collection name


# Helper function to validate email
def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None


# Helper function to validate phone number
def is_valid_phone(phone, country_code):
    """Validate phone number based on country code"""
    try:
        parsed_number = phonenumbers.parse(phone, country_code)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False


def is_valid_country(country_name):
    """Check if the country name exists in the pycountry database"""
    return country_name in [country.name for country in pycountry.countries]


def is_valid_postal_code(postal_code, country_name):
    """Validate postal code format based on country code"""
    # Example regex-based validation (adjust per country as needed)
    patterns = {
        "US": r"^\d{5}(-\d{4})?$",  # USA: 12345 or 12345-6789
        "Canada": r"^[A-Za-z]\d[A-Za-z] ?\d[A-Za-z]\d$",  # Canada: A1A 1A1
        "IN": r"^\d{6}$",  # India: 110001
    }
    pattern = patterns.get(country_name, r"^\d{4,10}$")  # Default pattern
    return bool(re.match(pattern, postal_code))


# Helper function to validate alphabetic fields (city, state, country)
def is_valid_text(value):
    return bool(re.match(r'^[A-Za-z\s\-]+$', value))  # Allows letters, spaces, and hyphens


# Routes
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/benefits')
def benefits():
    return render_template('benefits.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        # Validate required fields
        if not data.get('name') or not data.get('email') or not data.get('phone'):
            return jsonify({'message': 'Name, email, and phone are required'}), 400

        # Validate phone number with country code
        country = data.get('country', '').strip()
        phone = data.get('phone', '').strip()
        if not is_valid_phone(phone, country):
            return jsonify({'message': f'Invalid phone number for {country}'}), 400

        # Validate country name
        if not is_valid_country(country):
            return jsonify({'message': f'Invalid country name: {country}'}), 400

        # Validate postal code
        postal_code = data.get('postal', '').strip()
        if not is_valid_postal_code(postal_code, country):
            return jsonify({'message': f'Invalid postal code format for {country}'}), 400

        # Convert date string to a Python date object
        dob_str = data.get('dob')
        dob = None
        if dob_str:
            try:
                dob = datetime.strptime(dob_str, '%Y-%m-%d').date()

                if dob > date.today():
                    return jsonify({'message': 'Invalid DOB: Date cannot be in the future.'}), 400

            except ValueError:
                return jsonify({'message': 'Invalid date format. Use YYYY-MM-DD.'}), 400

        # Create a new user document
        new_user = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': phone,
            'dob': dob.isoformat() if dob else None,
            'street': data.get('street'),
            'city': data.get('city'),
            'state': data.get('state'),
            'postal': postal_code,
            'country': country,
            'institution': data.get('institution'),
            'student_id': data.get('student-id'),
            'message': data.get('message')
        }

        # Insert the new user into the MongoDB collection
        users_collection.insert_one(new_user)

        # Return a success response
        return jsonify({
            'message': 'Data submitted successfully!',
            'redirect': url_for('thank_you')
        })
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500


@app.route('/thank-you')
def thank_you():
    return render_template('thankyou.html')


if __name__ == '_main_':
    app.run(debug=True)