from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database to store users and offices
USERS = {
    "admin@example.com": {"password": "adminpass", "role": "Admin"},
    "scott@example.com": {"password": "scottpass", "role": "Custodian"}
}

OFFICES = []  # List of offices [{'name': 'Office1', 'assigned_to': 'scott@example.com'}, ...]

# Sign-up Route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"status": "error", "message": "Email and password are required"}), 400

    if email in USERS:
        return jsonify({"status": "error", "message": "User already exists"}), 409

    # Assign default role as Custodian for new sign-ups
    USERS[email] = {"password": password, "role": "Custodian"}
    return jsonify({"status": "success", "message": "User created successfully"}), 201

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = USERS.get(email)
    if user and user["password"] == password:
        return jsonify({"status": "success", "role": user["role"], "message": "Login successful"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401

# Create Office and Assign to User (Admin only)
@app.route('/create_office', methods=['POST'])
def create_office():
    data = request.json
    office_name = data.get('office_name')
    assigned_to = data.get('assigned_to')
    email = data.get('admin_email')  # Get the email of the admin creating the office

    if not office_name or not assigned_to:
        return jsonify({"status": "error", "message": "Office name and assigned user are required"}), 400

    # Check if the admin creating the office is authorized (must be Admin)
    admin = USERS.get(email)
    if not admin or admin['role'] != 'Admin':
        return jsonify({"status": "error", "message": "Only Admins can create offices"}), 403

    # Check if assigned user exists
    if assigned_to not in USERS:
        return jsonify({"status": "error", "message": "User not found"}), 404

    # Check if the office already exists
    if any(office['name'] == office_name for office in OFFICES):
        return jsonify({"status": "error", "message": "Office already exists"}), 409

    # Assign the office to the user
    OFFICES.append({"name": office_name, "assigned_to": assigned_to})
    return jsonify({"status": "success", "message": f"Office '{office_name}' assigned to {assigned_to}"}), 201

# Get Offices for a User
@app.route('/get_offices/<email>', methods=['GET'])
def get_offices(email):
    if email not in USERS:
        return jsonify({"status": "error", "message": "User not found"}), 404

    # Filter offices assigned to this user
    user_offices = [office for office in OFFICES if office['assigned_to'] == email]
    return jsonify({"status": "success", "offices": user_offices}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
