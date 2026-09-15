from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_command = data.get('command', '').lower()
    
    if 'hello' in user_command or 'hi' in user_command:
        reply = "Hello! How can I help you today?"
    elif 'time' in user_command:
        from datetime import datetime
        reply = f"Current time is {datetime.now().strftime('%H:%M')}"
    elif 'name' in user_command:
        reply = "I am Jarvis, your AI Web Assistant!"
    else:
        reply = f"I received your command: {user_command}"
        
    return jsonify({'response': reply})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

