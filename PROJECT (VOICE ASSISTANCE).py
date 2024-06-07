# PROJECT NAME: VOICE ASSISTANCE
# TEAM MEMBERS:
# IU2041222107 - HETANSHI AGRAWAL



import pyttsx3						
import speech_recognition as sr                         
import webbrowser                                       
import datetime                                        
import pyjokes
import os
import time
import string

def sptext():                                           
	recognizer=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listenting...")
		recognizer.adjust_for_ambient_noise(source)
		audio=recognizer.listen(source)
		try:
			print("Recognizing...")
			data=recognizer.recognize_google(audio)
			print(data)
			return data
		except sr.UnknownValueError:
			print("Sorry,Not able to recognize...")

def speechtx(x):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice',voices[1].id)
	rate = engine.getProperty('rate')
	engine.setProperty('rate',140)
	engine.say(x)
	engine.runAndWait()

if __name__== '__main__':

	
			while True:
					data1=sptext().lower()
					if "your name" in data1:
						name="my name is python"
						speechtx(name)
						print(name)

					elif "old are you" in data1:
						age = "i am one year old"
						speechtx(age)
						print(age)

					elif "time" in data1:
						time = datetime.datetime.now().strftime("%I%M%p")
						speechtx(time)
						print(time)

					elif "youtube" in data1:
						webbrowser.open("https://www.youtube.com/")

					elif "classroom" in data1:
						webbrowser.open("https://classroom.google.com/u/1/")

					elif "google" in data1:
						webbrowser.open("https://www.google.com/")

					elif "gmail" in data1:
						webbrowser.open("https://mail.google.com/mail/u/1/#inbox")

					elif "drive" in data1:
						webbrowser.open("https://drive.google.com/drive/u/1/my-drive")

					elif "joke" in data1:
						joke_1 = pyjokes.get_joke(language="en",category="neutral")
						print(joke_1)
						speechtx(joke_1)

					elif "song" in data1:
						add = "C:\songs" 
						listsong = os.listdir(add)
						print(listsong)
						os.startfile(os.path.join(add,listsong[1]))
						time.sleep(6)

					elif "exit" in data1:
						speechtx("thank you")
						break
					time.sleep(3)
					