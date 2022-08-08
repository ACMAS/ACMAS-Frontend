from django.core.cache import cache
from django.db.models.query import EmptyQuerySet
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import UploadedFile
from .search import searchFacade
from .upload import createFacade

# from django.core.files.storage import FileSystemStorage


# ACMAS homepage
@csrf_exempt
def index(request):
    return redirect("static/index.html")


# Search by question page
@csrf_protect
def searchByQuestion(request):
    question = request.POST.get("question")  # Check to see if a question was entered
    if (
        question is not None and len(question) > 0
    ):  # If a question was entered, ignore file input
        # Do manual question search logic here
        print("Manual question: ", question)
        # Instantiate and get session key
        sessionID = request.session._get_or_create_session_key()
        # Prevent session from client from changing until 20 minutes
        request.session.modified = True
        # If session has no facade, create one
        facade = cache.get(sessionID)
        if facade is None:
            cache.set(sessionID, searchFacade(), 1200)
            facade = cache.get(sessionID)
        # Search with Facade
        files = facade.searchQuestion(question)
        # Save facade state
        cache.set(sessionID, facade, 1200)
        return render(request, "search-results.html", {"files": files, "manual": True})
    # elif len(request.FILES) != 0:  # Check if a file was uploaded
    #     file = request.FILES["fileUpload"]  # Get the uploaded file
    #     fs = FileSystemStorage()
    #     filename = fs.save(file.name, file)  # Retrieve the filename
    #     file_url = fs.url(filename)  # Retrieve the file path

    # # Do question file upload logic here
    # print(f'FILE "{filename}" uploaded to "{file_url}"\n')
    return render(request, "search-by-question.html")


@csrf_exempt
def searchByCourse(request):
    return render(request, "search-by-course.html")


# Utilizes search by course form
@csrf_exempt
def searchResults(request):
    # Get input
    school = request.POST.get("school")
    course = request.POST.get("course")
    assignmentType = request.POST.get("type")

    # In case of no results ensure working html
    files = EmptyQuerySet
    # Check input
    if (
        school is not None
        and course is not None
        and len(school) > 0
        and len(course) > 0
    ):
        print("University:", school)
        print("Course:", course)
        print("Assignment Type:", assignmentType)
        # Instantiate and get session key
        sessionID = request.session._get_or_create_session_key()
        request.session.modified = True
        # If session has no facade, create one
        facade = cache.get(sessionID)
        if facade is None:
            cache.set(sessionID, searchFacade(), 1200)
            facade = cache.get(sessionID)
        files = facade.search(school, course, assignmentType)
        # Save facade state
        cache.set(sessionID, facade, 1200)

        # If the search input was valid
        if files is not None:
            return render(
                request, "search-results.html", {"files": files, "manual": False}
            )
    # If input was invalid
    return render(request, "search-results.html")


@csrf_exempt
def returnQuery(request):
    # Returns to previous query results
    # Getting current session facade
    sessionID = request.session._get_or_create_session_key()
    facade = cache.get(sessionID)

    # If there is no facade default to homepage
    if facade is None:
        return redirect("/")
    # Else return to previous query
    search_type = [False]
    resultsList = facade.getQuery(search_type)
    return render(
        request, "search-results.html", {"files": resultsList, "manual": search_type[0]}
    )


@csrf_protect
def pdfReader(request):
    name = request.GET.get("url")
    # If the file is a .txt load by filename
    if name[-4:] == ".txt":
        return render(request, "pdf-reader.html", {"directory": "../media/" + name})
    # Else obtain object from session Facade and display file
    sessionID = request.session._get_or_create_session_key()
    facade = cache.get(sessionID)

    # If session expired, or no search by course was made, or recent search does not contain file
    if (
        facade is None
        or facade.getQuery() is None
        or not facade.getQuery().filter(filename=name).exists()
    ):
        # Get file directly
        file = UploadedFile.objects.get(filename=name)
        return render(request, "pdf-reader.html", {"directory": file.file_dir})
    # Obtain pdf from last search and display
    file = facade.getQuery().get(filename=name)
    return render(request, "pdf-reader.html", {"directory": file.file_dir})


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
        assignmentType = request.POST.get("type")
        file = request.FILES["fileUpload"]  # Get the uploaded file
        createFacade().uploadPdf(school, course, assignmentType, file)
        print("School: ", school, "\nCourse: ", course)
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
        createFacade().uploadText(school, course, question, answer)
    return render(request, "upload-manually.html")
