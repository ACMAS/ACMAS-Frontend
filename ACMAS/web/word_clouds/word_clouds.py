import os
import cv2
import pytesseract

folderPath = "Reviews"
myRevList = os.listdir(folderPath)

for image in  myRevList:
    img = cv2.imread(f'{folderPath}/{image}')
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd=r'C:Program FilesTesseract-OCRtesseract.exe'
corpus = []
for images in myRevList:
    img = cv2.imread(f'{folderPath}/{images}')
    if img is None:
        corpus.append("Could not read the image.")
    else:
        rev = pytesseract.image_to_string(img)
        corpus.append(rev)
list(corpus)
corpus

import pandas as pd
data = pd.DataFrame(list(corpus), columns=['Review'])
data

import re
def clean(text):
    return re.sub('[^A-Za-z0-9" "]+', ' ', text)
data['Cleaned Review'] = data['Review'].apply(clean)
data

import nltk
from nltk.corpus import stopwords
nltk.download("punkt")
from nltk import word_tokenize
stop_words = stopwords.words('english')

final_list = []
for column in data[['Cleaned Review']]:
    columnSeriesObj = data[column]
    all_rev = columnSeriesObj.values

    for i in range(len(all_rev)):
        tokens = word_tokenize(all_rev[i])
        for word in tokens:
            if word.lower() not in stop_words:
                final_list.append(word)

with open(r"opinion-lexicon-Englishpositive-words.txt","r") as pos:
  poswords = pos.read().split("n")
with open(r"opinion-lexicon-Englishnegative-words.txt","r") as neg:
  negwords = neg.read().split("n")

import matplotlib.pyplot as plt
from wordcloud import WordCloud

pos_in_pos = " ".join([w for w in final_list if w in poswords])
wordcloud_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(pos_in_pos)
plt.imshow(wordcloud_pos)

neg_in_neg = " ".join([w for w in final_list if w in negwords])
wordcloud_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(neg_in_neg)
plt.imshow(wordcloud_neg)