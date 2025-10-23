import os
import speech_recognition as sr
import datetime
import webbrowser
import pyttsx3

#create engine for text to speech
engine = pyttsx3.init()
engine.setProperty("rate", 175)

#speech function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
#taking command
def take_command() -> str:
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You Said:", command)
            return command
        except Exception as e:
            print("Error recognizing speech:", e)
            return ""

#run assistant
def run_assistant():
    command = take_command()
    #if command has time word
    if 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The correct time is {time}")

    elif 'open notepad' in command:
        speak("Opening notepad")
        os.system('notepad')

    elif 'open youtube' in command:
        speak("Opening youtube")
        webbrowser.open("https://youtube.com")

    elif 'hey pandi' in command:
        query = command.replace("hey pandi", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Searching for {query}")
            webbrowser.open(url)
        else:
            speak("I am here to assist you")

    #stop assistance
    elif 'bye' in command or 'stop' in command:
        speak("Okay, bye bye, see you soon!")
        exit()
    else:
        speak("I am here to assist you. Ask something like 'open youtube', 'open notepad', and so on.")

#main function
if __name__ == "__main__":
    speak("Hey, hi Kiran! I am here to assist you. Ask something like 'open youtube', 'open notepad', and so on.")
    while True:
        run_assistant()