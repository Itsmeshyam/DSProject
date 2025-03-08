from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Ensure the database directory exists
database_dir = os.path.join(os.path.dirname(__file__), 'database')
os.makedirs(database_dir, exist_ok=True)


# Use an absolute path for the database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(database_dir, "user_data.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        new_user = User(name=data.get('name'), email=data.get('email'), message=data.get('message'))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Data submitted successfully!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error: {str(e)}'}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
