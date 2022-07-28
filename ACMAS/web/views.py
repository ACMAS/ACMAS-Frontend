from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# ACMAS homepage
@csrf_exempt
def index(request):
    return render(request, "index.html")


# Search by question page
@csrf_protect
def searchByQuestion(request):
    question = request.POST.get("question")  # Check to see if a question was entered
    if (
        question is not None and len(question) > 0
    ):  # If a question was entered, ignore file input
        # Do manual question search logic here
        print("Manual question: ", question)
    elif len(request.FILES) != 0:  # Check if a file was uploaded
        file = request.FILES["fileUpload"]  # Get the uploaded file
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)  # Retrieve the filename
        file_url = fs.url(filename)  # Retrieve the file path

        # Do question file upload logic here
        print(f'FILE "{filename}" uploaded to "{file_url}"\n')
    return render(request, "search-by-question.html")


# Search by course page
@csrf_protect
def searchByCourse(request):
    school = request.POST.get("school")  # Check to see if a school was entered
    course = request.POST.get(
        "course"
    )  # Check to see if a course name or course code was entered
    assignmentType = request.POST.get("type")  # Get query type
    if (
        school is not None
        and course is not None
        and len(school) > 0
        and len(course) > 0
    ):  # Only do search logic if school and course were entered
        # Do search logic here
        print(
            "School: ",
            school,
            "\nCourse: ",
            course,
            "\nAssignment type: ",
            assignmentType,
        )
    return render(request, "search-by-course.html")


def uploadOptions(request):
    return render(request, "upload-options.html")


@csrf_protect
def uploadOCR(request):
    school = request.POST.get("school")  # Check to see if a school was entered
    course = request.POST.get(
        "course"
    )  # Check to see if a course name or course code was entered

    if (
        len(request.FILES) != 0
        and school is not None
        and len(school) > 0
        and course is not None
        and len(course) > 0
    ):  # If a school and course were entered, and there is an uploaded file
        file = request.FILES["fileUpload"]  # Get the uploaded file
        print("School: ", school, "\nCourse: ", course)
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)  # Retrieve the filename
        file_url = fs.url(filename)  # Retrieve the file path
        print(f'FILE "{filename}" uploaded to "{file_url}"\n')
    return render(request, "upload-OCR.html")


@csrf_protect
def uploadManually(request):
    school = request.POST.get("school")  # Check to see if a school was entered
    course = request.POST.get(
        "course"
    )  # Check to see if a course name or course code was entered
    question = request.POST.get("question")  # Check to see if a question was entered
    answer = request.POST.get("answer")  # Check to see if an answer was entered

    if (
        question is not None
        and len(question) > 0
        and answer is not None
        and len(answer) > 0
        and school is not None
        and len(school) > 0
        and course is not None
        and len(course) > 0
    ):  # If a school, course, question, and answer were entered
        # Do manual question upload logic
        print(
            f"School: {school}\nCourse: {course}\nManual question: {question}\nManual answer: {answer}"
        )
    return render(request, "upload-manually.html")
