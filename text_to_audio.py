from gtts import gTTS
from playsound import playsound

audio = "outcome.mp3"
language = 'en'
speech = gTTS(text="Welcome to text to audio convertor",lang=language,slow=False)
speech.save(audio)  
playsound(audio)
print('sucuessfully running')

# from gtts import gTTS
# from playsound import playsound
#
# def text_to_audio(text, language='en', slow=False):
#     audio_file = "output.mp3"
#     speech = gTTS(text=text, lang=language, slow=slow)
#     speech.save(audio_file)
#     playsound(audio_file)
#
# if __name__ == "__main__":
#     user_input = input("Enter the text you want to convert to audio: ")
#     text_to_audio(user_input)
#     print('Successfully converted and played the audio.')
