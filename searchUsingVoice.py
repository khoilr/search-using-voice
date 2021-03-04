import wolframalpha
import wikipedia
import pyttsx3
import speech_recognition

client = wolframalpha.Client("THGPQH-UJ7YXT73VK")
engine = pyttsx3.init()

def talk(sentence):
    print(sentence)
    engine.say(sentence)
    engine.runAndWait()

def listen():
    recognize = speech_recognition.Recognizer()
    textAsVoiceInput = ''
    with speech_recognition.Microphone() as source:
        try: 
            print('Listenning')
            voiceInput = recognize.listen(source, timeout=5, phrase_time_limit=5)
            print('Done listen')
            textAsVoiceInput = recognize.recognize_google(voiceInput) #Trans from voice to text
        except speech_recognition.UnknownValueError as UnknownValueError: #Something that recognizer couldn't recognize
            print(UnknownValueError)
            talk("What are you saying?")
            pass
        except speech_recognition.WaitTimeoutError as WaitTimeoutError:  #Silent
            print(WaitTimeoutError)
            talk("You didn't say anything")
            pass
    return textAsVoiceInput

def lookUpOnWikipedia(sentence): 
    return wikipedia.summary(sentence)

def lookUpOnWolframAlpha(sentence): 
    result = client.query(sentence)
    return next(result.results).text

def lookup(sentence):
    try: #Wolfram Alpha's job
        return lookUpOnWolframAlpha(sentence)
    except: #Wolfram Alpha couldn't make it, how about Wikipedia?
        try:
            return lookUpOnWikipedia(sentence)
        except: #Wikipedia couldn't make it too
            return "I couldn't make it"

talk("What do you want me to look up?")
voiceInput = listen()
if voiceInput != '':
    print(voiceInput)
    res = lookup(voiceInput)
    talk(res)
    