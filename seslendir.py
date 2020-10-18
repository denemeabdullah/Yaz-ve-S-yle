from gtts import gTTS 
import os

while True:

    seslendir = input('Seslendirmek İstediğiniz Cümleyi Giriniz : ')

    tts = gTTS(text=seslendir, lang='tr')
    tts.save("ses.mp3")

    os.system("ses.mp3")
