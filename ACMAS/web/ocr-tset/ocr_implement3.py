from pyTesseract import Output
import pyTesseract
import cv2

filename = 'image_01.png'
image = cv2.imread(filename)

results = pyTesseract.image_to_data(image, 
output_type=Output.DICT)

{
'level': [1, 2, 3, 4, 5, 5, 5],
'page_num': [1, 1, 1, 1, 1, 1, 1],
'block_num': [0, 1, 1, 1, 1, 1, 1],
'par_num': [0, 0, 1, 1, 1, 1, 1],
'line_num': [0, 0, 0, 1, 1, 1, 1],
'word_num': [0, 0, 0, 0, 1, 2, 3],
'left': [0, 26, 26, 26, 26, 110, 216],
'top': [0, 63, 63, 63, 63, 63, 63],
'width': [300, 249, 249, 249, 77, 100, 59],
'height': [150, 25, 25, 25, 25, 19, 19],
'conf': ['-1', '-1', '-1', '-1', 97, 96, 96],
'text': ['', '', '', '', 'Testing', 'Tesseract', 'OCR']
}

for i in range(0, len(results[“text”])):
   x = results[“left”][i]
   y = results[“top”][i]

   w = results[“width”][i]
   h = results[“height”][i]

   text = results[“text”][i]
   conf = int(results[“conf”][i])

   if conf > 70:
       text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
       cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
       cv2.putText(image, text, (x, y - 10), 
cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

       cv2.imshow(image)