import speech_recognition as sr

def listen_and_convert():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening... Please say something.")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        # Capture the audio
        audio_data = recognizer.listen(source)
        print("Processing...")

        try:
            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")

if __name__ == "__main__":
    listen_and_convert()