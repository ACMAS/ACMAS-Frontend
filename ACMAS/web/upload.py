import os
import zlib

from datetime import date
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
        filename = fs.save(file.name, file)  # Retrieve the filename
        file_url = fs.url(filename)  # Retrieve the file path
        print(f'FILE "{filename}" uploaded to "{file_url}"\n')

        # Adding file to database
        db_file = UploadedFile(
            filename=filename,
            file_dir=file_url,
            course=Course.objects.get(name=course),
            date_uploaded=date.today(),
            flag=(fType),
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
        path = os.path.join(os.path.dirname(__file__), "..", "media")
        fileName = schoolName + "-" + courseName + "-" + hashString + ".txt"
        path = os.path.join(path, fileName)

        # Handling duplicate questions
        if os.path.exists(path):
            path = path[:-4] + "_1" + ".txt"
            fileName = fileName[:-4] + "_1" + ".txt"
        next_dupe = 2
        while os.path.exists(path):
            path = path[: path.rindex("_")] + "_" + str(next_dupe) + ".txt"
            fileName = fileName[: fileName.rindex("_")] + "_" + str(next_dupe) + ".txt"
            next_dupe += 1
        # Writing Question and Answer to file
        f = open(path, "x")
        f.write(f"QUESTION:\n-----------------------\n{question}\n")
        f.write("-----------------------\n\n\nANSWER:\n")
        f.write(f"-----------------------\n{answer}\n")
        f.write("-----------------------")
        f.close()

        # Entering file to database
        db_question = Question(
            filename=fileName,
            question=question,
            Answers=answer,
            Hash=hashString,
        )
        db_question.save()

        print(
            f"School: {uni}\nCourse: {course}\nManual question: {question}\nManual answer: {answer}\n"
            f"File name: {fileName}"
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
        if not University.objects.filter(name=uni).exists():
            new_uni = University(name=uni)
            new_uni.save()
            print("Created university:", uni)
        # If the course does not exist, create it
        if not Course.objects.filter(name=course).exists():
            new_course = Course(
                name=course,
                university=University.objects.get(name=uni),
            )
            new_course.save()
            print("Created course:", course)
