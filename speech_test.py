import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak something...")
    audio = recognizer.listen(source)
    print("🔄 Recognizing...")

    try:
        text = recognizer.recognize_google(audio)
        print("✅ You said:", text)
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("❌ Could not request results; check internet connection.", e)
