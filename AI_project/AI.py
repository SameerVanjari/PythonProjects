'''
Thingd to- do:
-play music
-open sites like youtube, webwhatsapp, wikipedia search, youtube search, search for anime releases, bas

TO-DO
- make a speak ffunc
- speech recog 
- web driver or seach 
- actions for opening files on system
'''
'''
Author: sam 
Purpose: a tool to do daily activities through voice commmands and automatically search for new video releases.

Date: 13/11/2020
'''
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12: speak("Good Morning Sam")
    elif hour>=12 and hour<17: speak("Good Afternoon Sam")
    else : speak("Good Evening Sam")
    speak("I am Sagittarius. Your personal assistant.")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
    
    try:
        print("Recognising... ")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User says: {query}")
    except Exception as e:
        # print(e)
        print("Error. Say that again please...")
        speak("Please, repeat")
        return "None"
    return query
        


if __name__ == "__main__":
    wish()
    while True:
        query = take_command().lower()

        # logic to execute tasks
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'quit' in query:
            exit()

        elif  'youtube' in query:
            webbrowser.open(url='https://youtube.com//')
        elif 'play music' in query:
            mu_dir = 'C:\\Users\\Sam\\Downloads\\Video'
            songs = os.listdir(mu_dir)
            print(f"Playing {songs[0]}")
            os.startfile(os.path.join(mu_dir, songs[0]))

        elif 'take note' in query:
            notepad = 'C:\\Users\\Sam\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories'
            prog = os.listdir(notepad)
            os.startfile(os.path.join(notepad, prog[0]))
            

    
