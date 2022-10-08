import zlib
from datetime import date

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from .models import Course, Question, University, UploadedFile


# Facade for uploading text questions/answers or a file
class createFacade:
    # Uploads pdf to database with given parameters
    def uploadPdf(self, uni, course, fType, file):
        """
        Parameters: String uni          - string of school/university name
                    String course       - string of course/class
                    String fType        - string designating upload type (Assignment, Exam, Practice)
                    request.FILE file   - UploadedFile object(not model) of file to upload
        """
        # If any entry doesn't exist raise exception
        if uni is None or course is None or file is None or fType is None:
            raise ValueError("Invalid input for file upload")
        # Perform upload
        fileEditHandler().uploadFile(uni, course, fType, file)

    # Parameters: All strings
    # uploadText: uploads question and its answer to database
    def uploadText(self, uni, course, question, answer):
        """
        Parameters: String uni          - string of school/university name
                    String course       - string of course/class
                    String question     - string containing the question
                    String answer       - string containing the answer
        """
        # If any entry doesn't exist raise exception
        if uni is None or course is None or question is None or answer is None:
            raise ValueError("Invalid input for question upload")
        # Perform upload
        questionEditHandler().uploadFile(uni, course, question, answer)


# Handles file upload
class fileEditHandler:
    # Method uploads file
    def uploadFile(self, uni, course, fType, file):
        """
        Parameters: String uni          - string of school/university name
                    String course       - string of course/class
                    String fType        - string designating upload type (Assignment, Exam, Practice)
                    request.FILE file   - UploadedFile object(not model) of file to upload
        """
        coursesEditHandler().prepare(uni, course)

        # Adding file to filesystem
        fs = FileSystemStorage()
        fileName = fs.get_available_name(file.name)
        savedFile = fs.save(fileName, file)  # Retrieve the filename
        file_url = fs.url(savedFile)  # Retrieve the file path
        print(f'FILE "{savedFile}" uploaded to "{file_url}"\n')

        # Adding file to database
        db_file = UploadedFile(
            File_Name=savedFile,
            File_Dir=file_url,
            Course=Course.objects.get(Name=course),
            Date_Uploaded=date.today(),
            Flag=fType,
        )
        db_file.save()


# Handles creation and upload of txt
class questionEditHandler:
    # Method uploads txt of questions with answers
    def uploadFile(self, uni, course, question, answer):
        """
        Parameters: String uni          - string of school/university name
                    String course       - string of course/class
                    String question     - string containing the question
                    String answer       - string containing the answer
        """
        # Ensure University and Course are valid
        coursesEditHandler().prepare(uni, course)

        # Formatting for filename creation
        schoolName = uni.replace(".", "").split(" ")[0]
        courseName = course.replace(" ", "_")
        hashString = str(zlib.crc32(bytes(question.encode("utf-8"))))

        # Creating file in filesystem
        fileName = schoolName + "-" + courseName + "-" + hashString + ".txt"
        fileText = (
            f"QUESTION:\n-----------------------\n"
            f"{question}\n-----------------------\n\n\nANSWER:"
            f"\n-----------------------\n{answer}\n"
            f"-----------------------"
        )
        fs = FileSystemStorage()
        # Returns a filename based on the name parameter that’s free and available for new content to be written to on
        # the target storage system
        djangoFileName = fs.generate_filename(fileName)
        fileContent = ContentFile(fileText)  # Set the content of the new file
        fs.save(djangoFileName, fileContent)  # Save file

        # Insert entry to the database
        db_question = Question(
            # File_Name=djangoFileName,
            # Question=question,
            File_Name=djangoFileName,
            Question=question,
            Answers=answer,
            Hash=hashString,
        )
        db_question.save()

        # Adding file to database
        db_file = UploadedFile(
            File_Name=fileName,
            File_Dir="/media/" + fileName,
            Course=Course.objects.get(name=course),
            Date_Uploaded=date.today(),
            Flag=(),
        )
        db_file.save()

        print(
            f"School: {uni}\nCourse: {course}\nManual question: {question}\nManual answer: {answer}\n"
            f"File name: {djangoFileName}"
        )


# Handles upload prerequisite code
class coursesEditHandler:
    # Ensures the University and Course exist
    def prepare(self, uni, course):
        """
        Parameters: String uni          - string of school/university name
                    String course       - string of course/class
        """
        # If the University does not exist, create it
        # if not University.objects.filter(Name=uni).exists():
        #     new_uni = University(Name=uni)
        if not University.objects.filter(Name=uni).exists():
            new_uni = University(Name=uni)
            new_uni.save()
            print("Created university:", uni)
        # If the course does not exist, create it
        # if not Course.objects.filter(Name=course).exists():
        if not Course.objects.filter(Name=course).exists():
            new_course = Course(
                # Name=course,
                # University=University.objects.get(Name=uni),
                Name=course,
                University=University.objects.get(Name=uni),
            )
            new_course.save()
            print("Created course:", course)
