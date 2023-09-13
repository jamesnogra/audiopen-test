from flask import Flask, render_template, request
import random
import string

# Audio to text function
from audio_to_text import convert_audio_to_text
# GPT
from gpt import summarize_transciption

app = Flask(__name__)

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
        if full_transcribed_text != 0:
            return {
                'full_transcribed_text': full_transcribed_text, # Uses recognize_google of speech_recognition
                'gpt_summary_text': summarize_transciption(full_transcribed_text) # Uses the model meta-llama/Llama-2-70b-chat-hf
            }, 200
        else:
            return full_transcribed_text, 200
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)