import os
import fitz  # PyMuPDF
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
    # the file type isn't pdf; returns ending type
    if ending_type(pdf_name) != 'pdf':
        return None

    print("CONVERTING PNG")

    if not os.path.isdir('mediafiles/ocr_images'):
        os.makedirs('mediafiles/ocr_images')

    image_names = []
    doc = fitz.open(pdf_name)
    for page_number in range(doc.page_count):
        page = doc.load_page(page_number)
        image = page.get_pixmap(matrix=fitz.Matrix(600/72, 600/72))
        image_name = f'mediafiles/ocr_images/page{page_number}.png'
        image.save(image_name, 'png')
        image_names.append(image_name)
    
    return image_names

def run_ocr(image_name):
    acceptable_formats = set({'png', 'jpg', 'gif', 'tiff'})
    if ending_type(image_name) not in acceptable_formats:
        return

    ocr_results = pytesseract.image_to_string(image_name, lang='eng')
    return ocr_results

def ocr_driver(pdf_name):
    if ending_type(pdf_name) == 'pdf':
        images = png_conversion(pdf_name)
    else:
        images = pdf_name
    ocr_output = []
    if isinstance(images, list):
        for image in images:
            ocr_output.append(run_ocr(image))
    else:
        ocr_output.append(run_ocr(images))
    return ocr_output


