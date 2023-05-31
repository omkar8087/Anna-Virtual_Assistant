import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
from tkinter import *
from PIL import Image, ImageTk
import wolframalpha
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    
    speak("I am Anna . please tell me how may I Help You sir")

root = Tk()
root.title('Anna')
root.geometry('520x320')
img = ImageTk.PhotoImage(file=r'C:\Users\Shubham\OneDrive\Desktop\Images\ANNA5.png')
panel = Label(root, image=img)
panel.pack(side='right', fill='both', expand='no')
userText = StringVar()
userText.set('Your Virtual Assistant')
userFrame = LabelFrame(root, text='Anna', font=('Railways', 24, 'bold'))
userFrame.pack(fill='both', expand='yes')
top = Message(userFrame, textvariable=userText, bg='black', fg='white')
top.config(font=("Century Gothic", 15, 'bold'))
top.pack(side='top', fill='both', expand='yes')
#btn = Button(root, text='Run', bg='red',fg='white').pack(fill='x', expand='no')
btn2 = Button(root, text='Close', bg='yellow',fg='black',command=root.destroy).pack(fill='x', expand='no')
root.mainloop()

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listenig...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising....")

        query = r.recognize_google(audio, language='en-in')

        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)

        print("say that again please...")
        return "None"
    return query 

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email.id','password')
    server.sendmail('email.id',to,content) 
    server.close()
    
if __name__== "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'Wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif'open youtube' in query:
            webbrowser.open ("youtube.com")

        elif'open google' in query:
            webbrowser.open("google.com")
       

        elif'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif'play music' in query:
            music_dir = 'A:\\movies\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now() .strftime("%H:%M: %S:")
            speak(f"sir, the time is {strTime}")
        
        elif 'open vlc' in query:
            codepath ="C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(codepath)
            
        elif 'email to shubham' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "en20179733@git-india.edu.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email") 

        elif'ask' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="K6EVRQ-HJ4A8H8V8U"
            client = wolframalpha.Client('K6EVRQ-HJ4A8H8V8U')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)  
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        
        

