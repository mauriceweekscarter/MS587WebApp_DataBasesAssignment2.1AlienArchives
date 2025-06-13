# Import required libraries
from flask import Flask, request, send_file
from gtts import gTTS
import io
import os

# Initialize Flask app
app = Flask(__name__)

# Define TTS endpoint
@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()  # Get JSON payload from frontend
    text = data['text']        # Extract text field

    # Use gTTS to generate speech directly into memory buffer
    tts = gTTS(text)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # Return audio file from memory directly to browser
    return send_file(mp3_fp, mimetype='audio/mpeg')

# Run Flask app locally on port 5000
if __name__ == '__main__':
    app.run(debug=True)





