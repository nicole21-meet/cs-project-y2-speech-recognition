import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
import webbrowser
import time



r=sr.Recognizer()
def record_audio(ask=False):
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data=''
	try:
		voice_data=r.recognize_google(audio)
	except sr.UnknownValueError:
		speak('sorry i did not get that')
	except sr.RequestError:
		speak('sorry an mot working')
	return voice_data

def speak(audio_string):
	tts= gTTS(text=audio_string, lang="en")
	r=random.randint(1,10000000)
	audio_file="audio-"+ str(r)+".mp3"
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)
#the function  takes the movie input compers is to
#the moive option
		
def movies(a,a2,b,b2,c,c2):
	hello=record_audio()
	print(hello)
	if a in hello:
		speak("you made a great movie choice hope you enjoy it")
		webbrowser.open(a2,new=1)
		exit()
	if b in hello:
		speak("you made a great movie choice hope you enjoy it")
		webbrowser.open(b2,new=1)
		exit()

	if c in hello:
		speak("you made a great movie choice hope you enjoy it")
		webbrowser.open(c2,new=1)
		exit()

def respond(voice_data):
	if "genres" in voice_data:
		speak("the genre's are: horror movies,romantic comdey, action,comdey and fantsy")
	if "horror movies" in voice_data:
		speak("the movies i recommend in this genre are: truth or dare, Annabelle and it. which one do you want to watch")
		movies("truth or dare","https://movies123.city/movies/truth-or-dare/","Annabelle",'https://123tvstream.club/watch-annabelle-comes-home-full-movie-online-on-fmovies-8580.html',"it","https://ww2.online0123movies.com/watch-it-2017-123movies-484.html")
	
	if "romantic comedy" in voice_data:
		speak("the movies i recommend in this genre are: love Simon, to all the boys i loved before and just go with it. which one do you want to watch")
		movies("love Simon","https://ww1.online123movies.live/watch-love-simon-2018-full-movie-free-123movies-721.html","to all the boys I Loved Before",'https://ww4.0123movie.net/movie/to-all-the-boys-ive-loved-before-25932.html',"just go with it","https://www11.123movieshub.one/movie/just-go-with-it-2011/")
	
	if "action" in voice_data:
		speak("the movies i recommend in this genre are: Fast and Furious, mission impossible and ride along. which one do you want to watch")
		movies("Fast and Furious","https://ww1.123movies11.com/movie/fast-furious/watching.html?ep=1&sv=7","mission impossible",'https://123moviesme.online/mission-impossible-1996/',"ride along","https://ww1.online123movies.live/watch-ride-along-2014-full-movie-free-123movies-hd-3-3546.html")

	if "fantsy" in voice_data:
		speak("the movies i recommend in this genre are: Harry Potter, Percy Jackson and Maleficent. which one do you want to watch")
		movies("Harry potter","https://123moviesto.live/search/harry+potter/","Percy Jackson",'https://123moviesto.live/movies/percy-jackson-the-olympians-the-lightning-thief/',"Maleficent","https://123moviesto.live/movies/maleficent/")
	
	if "comedy" in voice_data:
		speak("the movies i recommend in this genre are: The mask, Ted and mean girls. which one do you want to watch")
		movies("The mask","https://123moviesme.online/the-mask-1994/","Ted",'https://ww1.123movies11.com/movie/ted',"mean girls","https://ww1.123movies11.com/movie/mean-girls")

	if "I'm done" in voice_data:
		speak("thank you for using our servies have a good day")
		exit()

speak("Hi my name is Alfi and I want to recomend u good tv shows  what genre of movie do you wish to see?")

while 1:
	voice_data=record_audio()
	print(voice_data)	
	respond(voice_data)