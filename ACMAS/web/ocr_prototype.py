import os
from pdf2image import convert_from_path
import pytesseract


# Gets the ending types of files
def ending_type(string):
    index = string.rfind('.')
    return string[index + 1:]


def png_conversion(pdf_name):
    # makes sure we are only converting pdfs if
    # the file type isnt pdf returns ending type
    if (ending_type(pdf_name) == 'pdf'):
        pass
    else:
        return []

    print("CONVERTING PNG")
    os.system("mkdir ocr_misc/ocr_images")
    image_names = []
    images_from_path = convert_from_path(pdf_name)
    for i in range(len(images_from_path)):
        # Save pages as images in the pdf
        images_from_path[i].save('ocr_misc/ocr_images/' + 'page' + str(i) + '.jpg', 'JPEG')
        image_names.append('ocr_misc/ocr_images/' + 'page' + str(i) + '.jpg')
    return image_names


def run_ocr(image_names):
    ocr_results = []
    acceptable_formats = set({'png', 'jpg', 'gif', 'tiff'})
    for i in range(0, len(image_names)):
        if ending_type(image_names[i]) not in acceptable_formats:
            return
        print("RUNNING OCR FOR IMAGE {} OF {} NAMED {}".format(i, len(image_names), image_names[i]))
        ocr_results.append(pytesseract.image_to_string('{}'.format(image_names[i]), lang='eng'))

    return ocr_results

def ocr_driver(pdf_name):
    if ending_type(pdf_name) == 'pdf':
        images = png_conversion(pdf_name)
    else:
        images = [pdf_name]
    ocr_output = run_ocr(images)
    return ocr_output

if __name__ == '__main__':
    #This is just an example pdf to test the ocr. You can swap it with any pdf of your choosing
    pdf = './ocr-tset/test.png'
    result = ocr_driver(pdf)
    print(result)
