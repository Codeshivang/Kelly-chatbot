import pyttsx3
from datetime import datetime
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am kelly, sir, what work you will offer me?")


def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)

    except Exception as e:
        print(e)
        print("Say it again....")
        return "None"
    return query


if __name__ == "__main__":
    wish()
query = take().lower()

if 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

elif 'open google' in query:
            webbrowser.open("https://www.google.com")

elif 'open wikipedia' in query:
            webbrowser.open("https://www.wikipedia.org/")

elif 'open github' in query:
            webbrowser.open("https://github.com/")

elif 'open chatgpt' in query:
            webbrowser.open("https://chatgpt.com")

elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")

elif 'open telegram' in query:
            webbrowser.open("https://web.telegram.org")

elif 'play music' in query:
            webbrowser.open("https://www.spotify.com")

elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")

elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.com")

elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
print("thanks for using me !!")
