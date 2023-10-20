import fitz, os  # PyMuPDF

def extract_text_from_pdf(fileName):
    text = ''
    pdf_path = os.path.abspath(fileName)
    pdf_document = fitz.open(pdf_path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    return text

asdfasdfasf

def create_txtfile(fileName, text):
    removeExt = os.path.splitext(fileName)[0]
    file_Name = removeExt + ".txt"
    file_Path = ''
    with open(file_Name, "w", encoding="utf-8") as file:
        file.write(text)
    return file_Path
