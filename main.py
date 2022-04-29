import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import calendar
import pyaudio
import requests, json


def acceptcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
        except Exception as e:
            print(e)
            return 'None'
    return query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def welcome():
    speak("welcome I am kukku how may i help you")


def tellDay():
    day = datetime.date.today()
    speak(calendar.day_name[day.weekday()])
    print(calendar.day_name[day.weekday()])


def tellTime():
    time = datetime.datetime.now().strftime("%I:%H:%p")
    speak("current time is" + time)
    print("current time is" + time)


def weather(city):
    api_key = "890d71279cff2f88db12cb0e2c45ec6a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        res = round(current_temperature - 273)
        print(res)
        return str(res)
    else:
        print(" City Not Found ")


def take_query():
    welcome()
    while True:
        query = acceptcommand().lower()
        if 'kukku' in query:
            query.replace("kukku", '')
            continue
        if 'what day is it' in query:
            tellDay()
            continue
        elif 'tell me the time' in query:
            tellTime()
            continue
        elif 'open browser' in query:
            speak("opening chrome")
            webbrowser.open("www.google.com")
            continue
        elif 'play' in query:
            song = query.replace("play", '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
            continue
        elif 'search' in query:
            query = query.replace("search", '')
            pywhatkit.search(query)
            speak("searching result in google")
            continue
        elif 'from wikipedia' in query:
            speak("checking wikipedia")
            query = query.replace("from wikipedia", '')
            print("According to wikipedia" + wikipedia.summary(query, sentences=4))
            speak("According to wikipedia" + wikipedia.summary(query, sentences=4))
            continue
        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
            continue
        elif 'your name' in query:
            speak("I am Kukku")
            continue
        elif 'how are you' in query:
            speak("I am fine thank you")
            continue
        elif 'weather' in query:
            weather_api = weather("kakinada")
            speak("current temperature is" + weather_api + "degrees")
        elif 'see you again' in query:
            speak("Bye,have a nice day")
            exit()
        else:
            speak("could not hear properly")


if __name__ == '__main__':
    take_query()
