import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import which

def convert_audio_to_text(full_filename):
    AudioSegment.converter = which("ffmpeg")
    # Load the audio file using pydub
    audio = AudioSegment.from_file(full_filename, format="wav")
    # Convert pydub AudioSegment to raw audio data (bytes)
    audio_data = audio.raw_data
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_data) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_sphinx(audio)
        print("Transcript: " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error with the speech recognition service: {0}".format(e))

convert_audio_to_text('uploads/test.wav')