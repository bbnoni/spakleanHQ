from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://spaklean:P@ssword1@spaklean.mysql.pythonanywhere-services.com/spaklean$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('admin', 'custodian'), nullable=False)

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

# Create a user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "role": user.role} for user in users]), 200

# Create an office
@app.route('/offices', methods=['POST'])
def create_office():
    data = request.get_json()
    new_office = Office(office_name=data['office_name'])
    db.session.add(new_office)
    db.session.commit()
    return jsonify({"message": "Office created successfully"}), 201

# Get all offices
@app.route('/offices', methods=['GET'])
def get_offices():
    offices = Office.query.all()
    return jsonify([{"id": office.id, "office_name": office.office_name} for office in offices]), 200

# Create an assignment
@app.route('/assignments', methods=['POST'])
def create_assignment():
    data = request.get_json()
    new_assignment = Assignment(custodian_id=data['custodian_id'], office_id=data['office_id'])
    db.session.add(new_assignment)
    db.session.commit()
    return jsonify({"message": "Assignment created successfully"}), 201

# Get all assignments
@app.route('/assignments', methods=['GET'])
def get_assignments():
    assignments = Assignment.query.all()
    return jsonify([{
        "id": assignment.id,
        "custodian_id": assignment.custodian_id,
        "office_id": assignment.office_id
    } for assignment in assignments]), 200

if __name__ == '__main__':
    app.run(debug=True)
