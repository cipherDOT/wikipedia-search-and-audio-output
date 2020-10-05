# all imports for the program

import pygame, io, wikipedia
from gtts import gTTS

# the searching function
def search(query):
    result = wikipedia.summary(query).split('.')
    for line in result:
        return line

# the text to speech function

def speak(text):
    with io.BytesIO() as file:
        gTTS(text=text, lang='en').write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

# running of the program

if __name__ == '__main__':
    text = input("Enter the query: ")
    speak_text = search(text)
    print(speak_text)
    speak(speak_text)
