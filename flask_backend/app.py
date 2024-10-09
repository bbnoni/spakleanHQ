from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Configure the database connection using environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://spakleanhq_user:k26gCOWUdWorxyJPCVKv9xUo0YJupsj7@dpg-cs36hcrv2p9s738tlhmg-a.oregon-postgres.render.com/spakleanhq')
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
    custodian_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    office_id = db.Column(db.Integer, db.ForeignKey('office.id'), nullable=False)

# Routes
@app.route('/')
def home():
    return jsonify({"message": "Flask API is running"})

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    # Check if user exists
    user = User.query.filter_by(username=email, role=role).first()

    if user and user.password == password:
        return jsonify({"status": "success", "role": user.role, "message": "Login successful"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid credentials or role"}), 401

# Get all offices for a specific user
@app.route('/assignments/<username>', methods=['GET'])
def get_assignments(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    assignments = Assignment.query.filter_by(custodian_id=user.id).all()
    assigned_offices = [{"office_id": a.office_id, "office_name": Office.query.get(a.office_id).office_name} for a in assignments]
    return jsonify({"status": "success", "offices": assigned_offices}), 200

if __name__ == '__main__':
    app.run(debug=True)
