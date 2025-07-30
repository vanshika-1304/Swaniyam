import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
paused = False  # global pause flag

def speak(text):
    print(f"🗣️ Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        print("🔄 Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"🧠 You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was a network issue.")
        return ""

def handle_command(command):
    global paused

    if "pause" in command:
        paused = True
        speak("Assistant paused. Say 'resume' to continue.")
    elif "resume" in command:
        if paused:
            paused = False
            speak("Resuming assistant.")
        else:
            speak("I wasn't paused.")
    elif paused:
        print("🤐 Assistant is paused...")
        return
    elif "name" in command:
        speak("My name is Swaniyam, your assistant.")
    elif "how are you" in command:
        speak("I'm functioning as expected. How can I help you?")
    elif "joke" in command:
        speak("Why don’t scientists trust atoms? Because they make up everything!")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

# Main loop
while True:
    command = listen()
    if command:
        handle_command(command)
