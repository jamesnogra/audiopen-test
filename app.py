from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-and-transcribe-audio', methods=['POST'])
def upload_audio():
    try:
        # Get the audio file from the POST request
        audio_file = request.files['audio']
        # Save the audio file to a directory (e.g., 'uploads')
        audio_file.save('uploads/recorded_audio.wav')
        # Perform any processing on the audio file here, if needed
        return 'Audio uploaded successfully', 200
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True)