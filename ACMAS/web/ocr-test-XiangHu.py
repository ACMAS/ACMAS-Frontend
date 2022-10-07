from PIL import Image
import pytesseract
import numpy as np
from pdf2image import convert_from_path


filename1 = 'test.png'
img1 = np.array(Image.open(filename1))
text = pytesseract.image_to_string(img1)

#convert from pdf to png
pages = convert_from_path('test-ocr-pdf.pdf', 500)
for page in pages: #save png file
    page.save('pdf-to-png-out.png', 'PNG')

filename2 = 'pdf-to-png-out.png'
img2 = np.array(Image.open(filename2))
text2 = pytesseract.image_to_string(img2)

print(test)
print(text2)
