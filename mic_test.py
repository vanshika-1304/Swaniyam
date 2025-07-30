import speech_recognition as sr

recognizer = sr.Recognizer()

mic_index = 10  # Use the correct mic index from your list

print(f"Using input device index: {mic_index}")
with sr.Microphone(device_index=mic_index) as source:
    print("Recording... Speak now!")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Could not request results; check your internet connection.")
