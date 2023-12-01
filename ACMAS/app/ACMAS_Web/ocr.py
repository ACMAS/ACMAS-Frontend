import fitz  # PyMuPDF
import os
from datetime import date
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Course, UploadedFile


"""
OCR File Creation Pipeline:
    - When a file is uploaded to the filesystem, conduct OCR to extract and create text file
    - Check for name availability with created text file
    - Store text file on filesystem and database
"""
class OCR:
    def extract_text_from_pdf(self, fType, course, fileName, fileUrl):
        # Adding file to filesystem
        fs = FileSystemStorage()
        removeExt = os.path.splitext(fileName)[0]
        txt_file_name = removeExt + ".txt"
        txt_file_path = os.path.join(settings.MEDIA_ROOT, txt_file_name)
        text = ''
        pdf_document = fitz.open(fileUrl)
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
        with open(txt_file_path, "w", encoding="utf-8") as file:
            file.write(text)
        fs.save(fileName, txt_file_path)  # Retrieve the filename

        # Save the text content to the database using UploadedFile model
        uploaded_file = UploadedFile.objects.create(
            filename=txt_file_name,
            file_dir=txt_file_path,
            course=Course.objects.get(name=course),
            date_uploaded=date.today,
            flag=fType,  
        )
        uploaded_file.save()
