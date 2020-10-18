from gtts import gTTS 
import os

while True:

    seslendir = input('Seslendirmek İstediğiniz Cümleyi Giriniz : ')

    tts = gTTS(text=seslendir, lang='tr')
    tts.save("merhaba.mp3")

    os.system("merhaba.mp3")
