import requests
import speech_recognition as sr
import subprocess
from gtts import gTTS
import vlc

#sender = input("Hello!\n")

bot_message = ""
message = ""

#r = requests.post('http.//localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})
#
#print("Bot says, ", end=' ')
#for i in r.json():
#    bot_message = i['text']
#    print(f"{i['text']}")
#
#language = 'en'
#myobj = gTTS(text=bot_message, lang=language)
#myobj.save("hello.mp3")
#print('saved')
#
#player = vlc.MediaPlayer("/path/to/file.flac")
#vlcPath = "C:/Program Files/VideoLAN/VLC/vlc.exe"
#subprocess.run([vlcPath, "hello.mp3", '--play-and-exit'])

while bot_message != "Bye" or bot_message!='thanks':

    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("(Speak anything!)")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(message))

        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    if len(message)==0:
        continue

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says: ", end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message)
    myobj.save("hello.mp3")

    player = vlc.MediaPlayer("/path/to/file.flac")
    vlcPath = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    subprocess.call([vlcPath, "hello.mp3", '--play-and-exit'])



