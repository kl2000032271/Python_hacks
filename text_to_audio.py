#below code takes input is statically declared
from gtts import gTTS
from playsound import playsound

audio = "outcome.mp3"
language = 'en'
speech = gTTS(text="Welcome to text to audio convertor",lang=language,slow=False)
speech.save(audio)
playsound(audio)
print('sucuessfully running')



#below code takes input from console
from gtts import gTTS
from playsound import playsound

audio = "outcome.mp3"
language = 'en'
userinput = input()
speech = gTTS(text=userinput,lang=language,slow=False)
speech.save(audio)
playsound(audio)
print('sucuessfully running')
