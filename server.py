# Import required libraries
import pyttsx3
from flask import Flask, request, send_file
import os

# Initialize Flask app
app = Flask(__name__)

# Create folder to store generated audio files (if it doesn’t exist)
if not os.path.exists("audio"):
    os.makedirs("audio")

# Define TTS endpoint
@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data['text']

    # Use pyttsx3 to generate speech and save to a file
    engine = pyttsx3.init()
    engine.save_to_file(text, 'audio/output.mp3')
    engine.runAndWait()

    return send_file('audio/output.mp3', mimetype='audio/mpeg')

# Run Flask app locally on port 5000
if __name__ == '__main__':
    app.run(debug=True)



