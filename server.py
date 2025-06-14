# Import required libraries
from flask import Flask, request, jsonify
import pyttsx3
import os

app = Flask(__name__)

# Make sure audio directory exists
if not os.path.exists('audio'):
    os.makedirs('audio')

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data['text']

    output_path = 'audio/output.mp3'

    # Generate speech using pyttsx3 and save to file
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    engine.stop()

    # Return just the file path as JSON
    return jsonify({'file_url': f'/audio/output.mp3'})

# Serve static files from /audio folder
@app.route('/audio/<filename>')
def serve_audio(filename):
    return app.send_static_file(f'audio/{filename}')

if __name__ == '__main__':
    app.run(debug=True)







