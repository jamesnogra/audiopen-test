from flask import Flask, render_template, request
from flask_sslify import SSLify
from datetime import datetime
import random
import string
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
running_env = os.getenv('ENV')
running_port = os.getenv('PORT')

# Audio to text function
from audio_to_text import convert_audio_to_text
# GPT
from gpt import summarize_transciption

app = Flask(__name__)
if running_env == 'server':
    sslify = SSLify(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-and-transcribe-audio', methods=['POST'])
def upload_audio():
    try:
        filename = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        filename_save_as = f'uploads/{filename}.webm'
        # Get the audio file from the POST request
        audio_file = request.files['audio']
        # Save the audio file to a directory (e.g., 'uploads')
        audio_file.save(filename_save_as)
        # Transcribe audio
        full_transcribed_text = convert_audio_to_text(filename_save_as)
        gpt_summary_text, gpt_title = summarize_transciption(full_transcribed_text) # Uses the model meta-llama/Llama-2-70b-chat-hf
        # If error on the Llama model, try another model
        if gpt_title == 'Error':
            gpt_summary_text, gpt_title = summarize_transciption(full_transcribed_text)
        if full_transcribed_text != 0:
            return {
                'full_transcribed_text': full_transcribed_text, # Uses recognize_google of speech_recognition
                'gpt_summary_text': gpt_summary_text,
                'gpt_title': gpt_title,
                'date': datetime.today().strftime('%b %d, %Y')
            }, 200
        else:
            return 'Error', 200
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    if running_env == 'server':
        app.run(
            host='0.0.0.0',
            port=running_port,
            ssl_context=(
                "/etc/letsencrypt/live/www.iamcebu.com/fullchain.pem",
                "/etc/letsencrypt/live/www.iamcebu.com/privkey.pem"
            )
        )
    else:
        app.run(host='0.0.0.0', port=running_port, debug=True)