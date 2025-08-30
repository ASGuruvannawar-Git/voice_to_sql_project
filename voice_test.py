import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use the microphone
with sr.Microphone() as source:
    print("🎤 Say something...")
    audio = r.listen(source)   # listen to voice input

    try:
        text = r.recognize_google(audio)  # use Google's speech recognition
        print("✅ You said:", text)
    except sr.UnknownValueError:
        print("❌ Sorry, I could not understand your speech.")
    except sr.RequestError:
        print("❌ Could not request results, check your internet connection.")
