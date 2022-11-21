import pyautogui
import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import random
import time
import pywhatkit  as kit
from requests import get
import sys
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

# text to  speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Takes microphone input and returns string output
def takecommand():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 2
        audio = r.listen(source, timeout=1000, phrase_time_limit=5)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said:{query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# Wish
def wish():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak(f"Good Evening its {hour} sir")
    speak("I am jarvis , please tell me how can I help you")

if __name__ == '__main__':
    wish()
    while True:
        query = takecommand().lower()

    # logic building for tasks
        if "open notepad" in query:
            speak("opening notepad")
            path = "C:\\Windows\\notepad.exe"
            os.startfile(path)


        elif "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("What should I serach on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open facebook" in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")
        elif "play music" in query:
            path = "C:\\Users\\abc\\Desktop\\pahari songs"
            songs = os.listdir(path)
            print(songs)
            x = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(path,songs[x]))


        elif "the time" in query:
            strfTime  = datetime.datetime.now().strftime("%H %M ")
            speak(f"sir, the time is {strfTime}")

        elif "command prompt" in query:
            speak("Opening command prompt")
            os.system("Start cmd")




        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your ip address is {ip}")

        elif "send message" in query:
            kit.sendwhatmsg("+919736566940","This is testing the protocol",10,53)

        # TODO
        #  emil work is  pending(part1)

        elif "play song on youtube" in query:
            speak("Playing sir")
            pywhatkit.playonyt("see you again")

        elif "close notepad" in query:
             speak("ok sir, closing notepad")
             os.system("taskkill /im make.exe")
             sys.exit()

        elif "no thanks" in query:
            speak("ok,have a good day sir")
            sys.exit()


        elif "set alarm" in query:

            time = int(datetime.datetime.now().hour)
            if time == 12:
                path = "C:\\Users\\abc\\Desktop\\pahari songs"
                songs = os.listdir(path)
                os.startfile(os.path.join(path,songs[0]))

        elif "tell joke" in query:
            joke =pyjokes.get_joke()
            speak(joke)

        elif "shut down the sytem" in query:
            os.system('shutdown /s /t 5')

        elif "restart the system" in query:
            os.system('restart /r /t 5')

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyup("alt")

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
          ##  news()





