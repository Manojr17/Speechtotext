import speech_recognition as sr
import whisper
import os

def save_audio(audio_data, filename="your_audio.wav"):
    with open(filename, "wb") as f:
        f.write(audio_data.get_wav_data())


import speech_recognition as sr
import whisper
import os

def save_audio(audio_data, filename="your_audio.wav"):
    with open(filename, "wb") as f:
        f.write(audio_data.get_wav_data())


def whisper_transcribe(filename="your_audio.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    print(f"Detected Language: {result['language']}")
    print("Whisper Transcription:", result["text"])

def whisper_transcribe(filename="your_audio.wav"):
    model = whisper.load_model("base")

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("Audio file is empty or missing!")
        return

    try:
        result = model.transcribe(filename)
        if result is not None and 'text' in result:
            print(f"Detected Language: {result.get('language', 'Unknown')}")
            print("Whisper Transcription:", result["text"])
        else:
            print("Whisper failed to transcribe the audio.")
    except Exception as e:
        print(f"Whisper encountered an error: {e}")

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")

        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        print("Google Recognizer Output (Hindi):", text)

        save_audio(audio, "your_audio.wav")
        whisper_transcribe("your_audio.wav")

        os.remove("your_audio.wav")

    except sr.UnknownValueError:
        print("Sorry, could not understand your speech.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    recognize_speech()

def whisper_transcribe(filename="your_audio.wav"):
    model = whisper.load_model("base")

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("Audio file is empty or missing!")
        return

    try:
        result = model.transcribe(filename)
        if result is not None and 'text' in result:
            print(f"Detected Language: {result.get('language', 'Unknown')}")
            print("Whisper Transcription:", result["text"])
        else:
            print("Whisper failed to transcribe the audio.")
    except Exception as e:
        print(f"Whisper encountered an error: {e}")

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")

        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        print("Google Recognizer Output (Hindi):", text)

        save_audio(audio, "your_audio.wav")
        whisper_transcribe("your_audio.wav")

        os.remove("your_audio.wav")

    except sr.UnknownValueError:
        print("Sorry, could not understand your speech.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    recognize_speech()
