import subprocess
import speech_recognition as sr
import os

# Converts an audio file to text
def convert_audio_to_text(full_filename):
    wav_file = 'uploads/test.wav'
    # Convert first to PCM wav
    convert_wav_file(full_filename, wav_file)
    recognizer = sr.Recognizer()
    # Load the audio file using speech_recognition
    with sr.AudioFile(wav_file) as source:
        try:
            # Use the recognizer to recognize audio
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            deleteAudioFiles(full_filename, wav_file)
            print("Transcript: " + text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return 0
        except sr.RequestError as e:
            print("Error with the speech recognition service: {0}".format(e))
            return 0

# Converts to a PCM wav file
def convert_wav_file(input_file, output_file):
    try:
        # Run FFmpeg command to convert webm to WAV
        subprocess.run(['ffmpeg', '-i', input_file, '-f', 'wav', output_file, '-y'], check=True)
        print(f"Conversion complete: {input_file} -> {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("FFmpeg not found. Please install FFmpeg and make sure it's in your system's PATH.")

# deletes the webm and wav file generated
def deleteAudioFiles(full_filename, wav_file):
    os.remove(full_filename)
    os.remove(wav_file)