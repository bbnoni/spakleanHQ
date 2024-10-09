from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# Configure the database connection using environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://spakleanhq_user:k26gCOWUdWorxyJPCVKv9xUo0YJupsj7@dpg-cs36hcrv2p9s738tlhmg-a.oregon-postgres.render.com/spakleanhq'
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

if __name__ == '__main__':
    app.run(debug=True)
