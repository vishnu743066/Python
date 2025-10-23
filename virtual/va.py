#first basic step is sppech to text
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time
from time import ctime
import re
import requests
import webbrowser
import bs4
import smtplib #simple mail transfer protocol


#to make its listens
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source,phrase_time_limit=5)
    data = ""

#expection handling
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data

#listen()

def respond(String):
    print(String)
    tts=gTTS(text=String,lang='en')
    tts.save('speech.mp3')
    playsound.playsound('speech.mp3')
    os.remove('speech.mp3')

def voice_assistant(data):
    """giving your actions"""
    if "how are you" in data:
        listening = True
        respond("Good and doing well")
    if "time" in data:
        listening = True
        respond(ctime())
    if "open google" in data.casefold():
        listening = True
        reg_ex=re.search('open google(.*)',data)
        url='https://www.google.com/'
        if reg_ex:
            sub=reg_ex.group(1)
            url = url+'r/'
        webbrowser.open(url)
        respond('Done')
        
    if "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen()
        edict = {'hello':'pabo21314.cs@rmkec.ac.in'}
        toaddr = edict[to]
        respond("what is the subject? ")
        subject = listen()
        respond("what should i tell that person? ")
        message=listen()
        content = 'Subject : {}\n\n{}'.format(subject,message)

        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('vv743066@gmail.com','bxbz ytwf icae tmqe')
        mail.sendmail('pabo21314.cs@rmkec.ac.in',toaddr,content)
        mail.close()
        respond('email sent')

    if "wiki" in data.casefold():
        lisening = True
        respond("What should i search")
        query= listen()
        response = requests.get('https://www.wikipedia.org/wiki/'+query)
        if response is not None:
            html = bs4.BeautifulSoup(response.text,'html.parser')
            paragraphs = html.select('p')
            intro = [i.text for i in paragraphs]
            halo = ' '.join(intro)
        respond(halo[:200])

    if "stop" in data:
        listening = False
        print("Listening Stopped")
        respond("see you vishnu")

    try:
        return lisening
    except UnboundLocalError:
        print("Timed Out")
        
#time.sleep(2)
respond("Hey vishnu how are you?")
listening = True
while listening == True:
    data = listen()
    listening = voice_assistant(data)
