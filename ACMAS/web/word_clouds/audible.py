import cv2
import pytesseract
from gtts import gTTS
import os
rev = cv2.imread("Reviews\15.PNG")

txt = pytesseract.image_to_string(rev)
print(txt)
language = 'en'
outObj = gTTS(text=txt, lang=language, slow=False)
outObj.save("rev.mp3")
print('playing the audio file')
os.system('rev.mp3')