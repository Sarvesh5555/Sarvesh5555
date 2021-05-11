import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=2)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sana' in command:
                command = command.replace('sana', '')
                print(command)
    except:
        pass
    return command


def run_sana():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'hi' in command:
        talk('Hi Sarvesh')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'love' in command:
        talk('I like his hair style')

    elif 'are you single' in command:
        talk('I am in a relationship with vikash')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'vikas' in command:
        talk('He is My Boyfriend')
    elif 'bye' in command:
        talk('See You Later Sir')
        print('BYEEE')
    else:
        talk('Please say the command again.')


while True:
    run_sana()