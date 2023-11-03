import tkinter as tk
from tkinter import Text,Scrollbar
import wave
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
from gtts import gTTS
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyaudio
import sys

import pyaudio
from distillargev2 import speech_recognizer

def record_audio():
    # CHUNK = 1024
    # FORMAT = pyaudio.paInt16
    # CHANNELS = 2
    # RATE = 44100
    # RECORD_SECONDS = 5

    # # Set up the audio stream
    # p = pyaudio.PyAudio()

    # stream = p.open(
    #     format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    # )

    # print("Speak...")

    # frames = []

    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #     data = stream.read(CHUNK)
    #     frames.append(data)

    # print("Voice recorded.")

    # stream.stop_stream()
    # stream.close()
    # p.terminate()

    # # Save the recorded audio to a WAV file (optional)
    # output_file = "output.wav"

    # wf = wave.open(output_file, "wb")
    # wf.setnchannels(CHANNELS)
    # wf.setsampwidth(p.get_sample_size(FORMAT))
    # wf.setframerate(RATE)
    # wf.writeframes(b"".join(frames))
    # wf.close()
   

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 if sys.platform == 'darwin' else 2
    RATE = 44100
    RECORD_SECONDS = 5

    with wave.open('output.wav', 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...')
        for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
            wf.writeframes(stream.read(CHUNK))
        print('Done')

        stream.close()
        p.terminate()


def TakeCommand():


    record_audio()


    # recognizer = sr.Recognizer()
    # audio_file = sr.AudioFile("output.wav")
    

    # with audio_file as source:
    #     audio_data = recognizer.record(source)

    try:
        # recognized_text = recognizer.recognize_google(audio_data) 
        recognized_text = speech_recognizer("C:/Users/vishn/Downloads/Da/output.wav")
        return recognized_text # Use Google Web API for speech recognition
        # print("Recognized text: " + recognized_text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web API; {0}".format(e))
    # r = sr.Recognizer()

    # with open("output.wav", "rb") as audio:
    #     query = r.recognize_google(audio, language='en-in')

    #     if transcribed_text is None:
    #             transcribed_text = ""
    #     os.remove("output.wav")
    #     print(f"User: {transcribed_text}")
    
    # return query

    #         print("the command is printed=", query)
    # r = sr.Recognizer()
    # r.pause_threshold = 0.9
    # with sr.Microphone() as source:
    #     print('Listening')

    #     # seconds of non-speaking audio before
    #     # a phrase is considered complete
    #     r.pause_threshold = 0.7
    #     audio = r.listen(source)

    #     print("owndoiawndion")

    #     # Now we will be using the try and catch
    #     # method so that if sound is recognized
    #     # it is good else we will have exception
    #     # handling
    #     try:
    #         print("Recognizing")

    #         # for Listening the command in indian
    #         # english we can also use 'hi-In'
    #         # for hindi recognizing
    #         query = r.recognize_google(audio, language='en-in')
    #         print("the command is printed=", query)

    #     except Exception as e:
    #         print(e)
    #         print("Say that again sir")
    #         return "None"

    #     return query

def Speak(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(audio)
    engine.runAndWait()


def execute_command():
    user_input = text_entry.get("1.0", "end-1c").lower()

    if "open youtube" in user_input:
        Speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")

    if "leo" in user_input:
        Speak("endrum    thala pathy  ")
        webbrowser.open("https://open.spotify.com/track/1B02UI29t3PTh3m98absaP")

    elif "what day is it?" in user_input:
            Speak("the day is")
            tellDate()
    
    elif "what time is it now?" in user_input:
            speak_time()



    # Add other commands here

    else:
        speak("Command not recognized")

def tellDate():
    # day= datetime.datetime.today().weekday()
    # Day_dict={1:"Monday",
    #           2:"Tuesday",
    #           3:"Wednesday",
    #           4:"Thursday",
    #           5:"Friday",
    #           6:"Saturday",
    #           7:"Sunday"
    #           }
    # if day in Day_dict.keys():
    #     day_of_the_week=Day_dict[day]
    #     print(day_of_the_week)

    x = datetime.datetime.now()
    day = x.strftime("%A")
    print(day)
    Speak("the day is"+ day)
"""
def telltime():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    #time_message = "The time is " + current_time
    #Speak(time_message)
    return current_time
"""

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")  # Format the time as "hh:mm AM/PM"
    print(current_time)
    return current_time

def speak_time():
    current_time = tell_time()
    Speak("The current time is " + current_time)

    """
    time=str(datetime.datetime.now())
    print(time)
    #2023/10/17 08:37:15:15642
    hour=time[11:13]
    minute=time[14:16]
    second=time[17:19]
    time_message="the time is"+ hour +"hours and"+ minute +"minutes and"+ second +"seconds"
    Speak(time_message)
    #Speak( "The time is sir" + hour + "Hours and" + min + "Minutes")
    """
def Hello():
    Speak("hello I am park hyung sik,your desktop assistant. how may i help you? innaikum then da ma  irukiya? padi daaa para maa! by the way where is bong soon?")

def speak(text):
    #tts = gTTS(text=text, lang='en')
    #tts.save("output.mp3")
    #os.system("mpg321 output.mp3")
    time=datetime.datetime.now().strftime('%H:%M %p')
    return time
def speaks():
    time=speak()
    Speak("time is "+time)


def send_email(to,subject,message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        email = "bhuma1970@gmail.com"
        password = "Mala&Mohan@70"
        server.login(email, password)

        # Compose the email
        email_message = f"Subject: {subject}\n\n{message}"

        # Send the email
        server.sendmail(email, to, email_message)

        # Close the server
        server.quit()
        print("Email sent successfully")
        speak("Email sent successfully")
        #server.login("madhumidhra104@gmail.com", "Abidhra@11")

    except Exception as e:
        print(e)
        print(f"An error occurred: {str(e)}")
        Speak("Sorry, I couldn't send the email. Please try again.")


def TakeQuery():
    Hello()

    while(True):
        query=TakeCommand()
        if query != None:
            query = query.lower()
            print(query)

        if "open youtube" in query:
            Speak("opening youtubeee")
            webbrowser.open("https://www.youtube.com/")
            continue

        elif "test" in query:
            Speak("hello this is test because naan  oru  thandam!")

        elif "send mail" in query:
            Speak("Whom do you want to send the email to?")
            to = TakeCommand().lower()
            speak("What is the subject of the email?")
            subject = TakeCommand().lower()
            speak("What message do you want to send?")
            message = TakeCommand()

            send_email(to, subject, message)
            continue

        elif "open google" in query:
            Speak("oopening Googleee")
            webbrowser.open("https://www.google.co.in/")
            continue

        elif "open spotify" in query:
            Speak("inimaiyana paadaluku opening spotify")
            webbrowser.open("https://open.spotify.com/")
            continue

        elif "leo" in query:
            Speak("endrum    thala pathy  ")
            webbrowser.open("https://open.spotify.com/track/1B02UI29t3PTh3m98absaP")
            continue

        elif "what time is it now?" in query:
            speaks()
            continue

        elif "what day is it?" in query:
            Speak("the day is")
            tellDate()
            continue

        elif "bye" in query:
            Speak("bye ping me if needed")
            break

        elif "tell me your name" in query:
            Speak("I am Park Hyung Sik.Your desktop assistant.but where is my bong soon")
            print("I am Park Hyung Sik.Your desktop assistant.bong soon?")
def execute_button():
    execute_command()

def Recognize_button():
    TakeQuery()

window = tk.Tk()
window.title("Desktop Assistant")

# Create a text entry field
text_entry = Text(window, height=4, width=50)
text_entry.pack()

# Create a scroll bar
scroll = Scrollbar(window)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Bind the scroll bar to the text entry
text_entry.config(yscrollcommand=scroll.set)
scroll.config(command=text_entry.yview)

# Create an "Execute" button
button = tk.Button(window, text="Execute Command", command=execute_command)
button.pack()

recognize_button = tk.Button(window, text="Recognize Voice", command=Recognize_button)
recognize_button.pack()

# Run the tkinter window
window.mainloop()

if __name__== '__main__':
    TakeQuery()



"""
  with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.7
        audio=r.listen(source)

        try:
            print("Recognizing..")
            query=r.recognize_google(audio,language='en-us')
            print("the command is printed=",query)
        except Exception as e:
            print(e)
            print("Could you please repeat?")
            return "none"
        return query

  Speak("To whom do you want to send mail?")
        to = TakeCommand().lower()
        to = "receiver@gmail.com"

        Speak("whatshould i include as subject?")
        subject = TakeCommand()

        Speak("what should i include as body?")
        body = TakeCommand()

        msg = MIMEMultipart()
        msg['From'] = "madhumidhra104@gmail.com"
        msg['to'] = to
        msg['subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()
        server.sendmail("madhumidhra104@gmail.com", to, body)
        server.quit()
        Speak("email sent successfully!")     

"""



