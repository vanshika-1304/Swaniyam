import speech_recognition as sr

# List all available microphones
mic_list = sr.Microphone.list_microphone_names()

print("Available microphones:")
for i, mic in enumerate(mic_list):
    print(f"{i}: {mic}")
