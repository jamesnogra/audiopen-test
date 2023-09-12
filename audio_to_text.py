import subprocess
import speech_recognition as sr

def convert_audio_to_text(full_filename):
    # Convert first webm to PCM wav
    convert_webm_to_wav(full_filename, 'uploads/test.wav')
    recognizer = sr.Recognizer()
    # Load the audio file using speech_recognition
    with sr.AudioFile('uploads/test.wav') as source:
        try:
            # Use the recognizer to recognize audio
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            print("Transcript: " + text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error with the speech recognition service: {0}".format(e))

def convert_webm_to_wav(input_file, output_file):
    try:
        # Run FFmpeg command to convert webm to WAV
        subprocess.run(['ffmpeg', '-i', input_file, '-f', 'wav', output_file, '-y'], check=True)
        print(f"Conversion complete: {input_file} -> {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("FFmpeg not found. Please install FFmpeg and make sure it's in your system's PATH.")