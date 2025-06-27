import speech_recognition as sr
import pyaudio

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Reduced duration for speed
        print("Listening... Speak clearly into the microphone.")

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing audio...")

            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text

        except sr.WaitTimeoutError:
            print("No speech detected within 5 seconds.")
            return None
        except sr.UnknownValueError:
            print("Sorry, couldn’t make out what you said.")
            return None
        except sr.RequestError as e:
            print(f"API request failed; check your internet: {e}")
            return None

def main():
    print("Speech-to-Text Converter")
    print("-----------------------")
    while True:
        input("Press Enter to start speaking (or Ctrl+C to quit)...")
        result = speech_to_text()
        if result:
            print("Transcription:", result)
        print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPeace out!")
