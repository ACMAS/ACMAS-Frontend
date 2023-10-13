import os
from pdf2image import convert_from_path
import pytesseract

absolute_path = os.path.dirname(__file__)
relative_path = "../ocr_files/lib"
full_path = os.path.join(absolute_path, relative_path)


# Gets the ending types of files
def ending_type(string):
    index = string.rfind('.')
    return string[index + 1:]


def png_conversion(pdf_name):
    # makes sure we are only converting pdfs if
    # the file type isnt pdf returns ending type
    if ending_type(pdf_name) != 'pdf':
        return None

    print("CONVERTING PNG")

    if not os.path.isdir('mediafiles/ocr_images'):
        os.system("mkdir mediafiles/ocr_images")

    image_names = []
    images_from_path = convert_from_path(pdf_name)
    for i in range(len(images_from_path)):
        # Save pages as images in the pdf
        images_from_path[i].save('mediafiles/ocr_images/' + 'page' + str(i) + '.jpg', 'JPEG')
        image_names.append('mediafiles/ocr_images/' + 'page' + str(i) + '.jpg')
    return image_names


def run_ocr(image_name):
    acceptable_formats = set({'png', 'jpg', 'gif', 'tiff'})
    if ending_type(image_name) not in acceptable_formats:
        return
    ocr_results = pytesseract.image_to_string('{}'.format(image_name), lang='eng')
    return ocr_results


def ocr_driver(pdf_name):
    if ending_type(pdf_name) == 'pdf':
        images = png_conversion(pdf_name)
    else:
        images = pdf_name
    ocr_output = run_ocr(images)
    return ocr_output