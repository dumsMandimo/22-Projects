#pip install SSpeechRecognition to install speech recog.

import speech_recognition as speech 
import webbrowser as web

#creating 3 instances
r1 = speech.Recognizer()
r2 = speech.Recognizer()
r3 = speech.Recognizer()

with speech.Microphone() as source: #this is source
    print("[search youtube: ]")
    print("Speak now")
    audio = r3.listen(source) #souorce is microphone
 
if 'video' in r1.recognize_google(audio):
    r1 = speech.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with speech.Microphone() as source:
        print("Search your query")
        audio = r1.listen(source)


        try:
            get = r1.recognize_google(audio)
            print(get)
            web.get().open_new(url+get) #gets query

        except speech.UnknownValueError: #passing exceptions
            print("error")

        except speech.RequestError as er:
            print("failed".format(er))

