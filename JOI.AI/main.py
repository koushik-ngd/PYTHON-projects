import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import midi2voice

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
            print('I am listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower() # type: ignore
            if 'joi' in command:
                command = command.replace('joi', '')
                print(command)
    except:
        pass
    return command # type: ignore


def run_joi():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '') # type: ignore
        talk('playing' + song)
        pywhatkit.playonyt(song) # type: ignore
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is ', '') # type: ignore
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'joi' in command:
        talk('yes , how may i help you?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'name' in command:
        talk('my name is joi, a virtual a i assistant')
    elif 'hello' in command:
        talk('hey, good to see you here')
    elif 'owner' in command:
        talk('the owner name is Koushik, born on 30th of april, 2004')
    elif 'doing' in command:
        talk('i am talking to you')
    elif 'help' in command:
        talk('how may i help you?')
    elif 'yourself' in command:
        talk('well,i am joi, a virtual assistant. i do certain tasks on which you can find me reliable on')
    elif 'bye' in command:
        talk('take care, it was nice talking to you. see you again')
    elif 'thank you' in command:
        talk('you are most welcome. let me assist you if you need any help')
    else:
        talk('Sorry I could not catch that')


while True:
    run_joi()




