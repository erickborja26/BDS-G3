from gtts import gTTS
import os

texto = input('Escribe un texto a conertir: ')
tts= gTTS(text=texto, lang='es')
filename= 'textoconvertido.mp3'
tts.save(filename)
os.system(f'start {filename}')