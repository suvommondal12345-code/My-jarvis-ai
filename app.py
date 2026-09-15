from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask_jarvis():
    data = request.get_json() or {}
    command = data.get("command", "").lower()
    
    if "time" in command or "সময়" in command:
        current_time = time.strftime("%I:%M %p")
        reply = f"এখন সময় {current_time}"
    elif "weather" in command or "আবহাওয়া" in command:
        reply = "আজকের আবহাওয়া রৌদ্রোজ্জ্বল।"
    else:
        reply = "আমি দুঃখিত, আপনার কথাটি বুঝতে পারিনি।"
        
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
