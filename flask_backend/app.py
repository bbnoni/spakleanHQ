from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://your_database_url_here'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)

class Office(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    office_name = db.Column(db.String(255), nullable=False)

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    office_id = db.Column(db.Integer, db.ForeignKey('office.id'), nullable=False)

# Create a user
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

# Create an office and assign it to a user
@app.route('/create_office', methods=['POST'])
def create_office():
    data = request.get_json()
    new_office = Office(office_name=data['office_name'])
    db.session.add(new_office)
    db.session.commit()

    user = User.query.filter_by(username=data['assigned_to']).first()
    if user:
        assignment = Assignment(user_id=user.id, office_id=new_office.id)
        db.session.add(assignment)
        db.session.commit()

    return jsonify({"message": "Office created and assigned"}), 201

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "role": user.role} for user in users]), 200

if __name__ == '__main__':
    app.run(debug=True)
