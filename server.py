# Import required libraries
import pyttsx3
from flask import Flask, request, send_file
import threading
import os

# Initialize Flask app
app = Flask(__name__)

# Create folder to store generated audio files (if it doesn't exist)
if not os.path.exists("audio"):
    os.makedirs("audio")

# Background TTS function to avoid run loop conflict
def tts_background(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'audio/output.mp3')
    engine.runAndWait()

# Define TTS endpoint
@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data['text']

    # Start pyttsx3 inside a separate thread
    thread = threading.Thread(target=tts_background, args=(text,))
    thread.start()
    thread.join()

    # Return the audio file back to browser
    return send_file('audio/output.mp3', mimetype='audio/mpeg')

# Run Flask app locally on port 5000
if __name__ == '__main__':
    app.run(debug=True)
