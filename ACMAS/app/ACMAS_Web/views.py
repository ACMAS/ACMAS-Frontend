import os

from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import redirect, render

from .forms import RegisterForm
from .models import UploadedFile
from .search import searchFacade
from .upload import createFacade


def generateContext(request):
    context = {
        "GOOGLE_ADSENSE_URL": os.getenv("GOOGLE_ADSENSE_URL", default="")
        + os.getenv("GOOGLE_ADSENSE_ID", default=""),
        "GOOGLE_ANALYTICS_ID": os.getenv("GOOGLE_ANALYTICS_ID", default=""),
        "GOOGLE_ANALYTICS_URL": os.getenv("GOOGLE_ANALYTICS_URL", default="")
        + os.getenv("GOOGLE_ANALYTICS_ID", default=""),
        "CANONICAL_PATH": request.build_absolute_uri(request.path),
    }
    return context


# ACMAS homepage
def index(request):
    context = generateContext(request)
    return render(request, "index.html", context)


# ACMAS Sitemap.xml file (used for Google Search Console)
def sitemap(request):
    return redirect("static/sitemap.xml")


# ACMAS robots.txt file (used for SEO and web crawlers)
def robots(request):
    return redirect("static/robots.txt")


# ACMAS favicon.ico logo (used for browser tab icon)
def favicon(request):
    return redirect("static/img/favicon.ico")


# Search by question page
def searchByQuestion(request):
    context = generateContext(request)
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

        context.update({"files": files, "manual": True})
        return render(request, "search-results.html", context)
    return render(request, "search-by-question.html", context)


def searchByCourse(request):
    context = generateContext(request)
    return render(request, "search-by-course.html", context)


# Utilizes search by course form
def searchResults(request):
    context = generateContext(request)

    # Get input
    school = request.POST.get("school")
    course = request.POST.get("course")
    assignmentType = request.POST.get("type")

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
            context.update({"files": files, "manual": False})
            return render(request, "search-results.html", context)
    # If input was invalid
    return render(request, "search-results.html", context)


def returnQuery(request):
    context = generateContext(request)

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
    context.update({"files": resultsList, "manual": search_type[0]})
    return render(request, "search-results.html", context)


def pdfReader(request):
    context = generateContext(request)

    name = request.GET.get("url")
    if "." in name:
        file_extension = name.rsplit(".")[1]
    else:
        file_extension = ""
    if file_extension == "txt":  # If the file is a .txt load by filename
        context.update({"directory": "../media/" + name})
        return render(request, "pdf-reader.html", context)
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
        context.update({"directory": file.file_dir})
        return render(request, "pdf-reader.html", context)
    # Obtain pdf from last search and display
    file = facade.getQuery().get(filename=name)
    context.update({"directory": file.file_dir})
    return render(request, "pdf-reader.html", context)


@login_required(login_url="/login")
def uploadFile(request):
    context = generateContext(request)

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

        if request.user.groups.filter(name="APO").exists():
            createFacade().uploadPdf(school, course, assignmentType, file, True)
        else:
            createFacade().uploadPdf(school, course, assignmentType, file, False)

    return render(request, "upload-file.html", context)


@login_required(login_url="/login")
def uploadManually(request):
    context = generateContext(request)

    school = request.POST.get("school")  # Check to see if a school was entered
    course = request.POST.get(
        "course"
    )  # Check to see if a course name or course code was entered
    question = request.POST.get("question")  # Check to see if a question was entered
    answer = request.POST.get("answer")  # Check to see if an answer was entered
    assignment_type = request.POST.get("type")  # Retrieve the assignment type
    verified = request.POST.get("verified")

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
        if request.user.groups.filter(name="APO").exists():
            createFacade().uploadText(
                school, course, question, answer, assignment_type, True
                )
            print("School: ", school, "\nCourse: ", course)
        else:
            createFacade().uploadText(
                school, course, question, answer, assignment_type, False
                )
            print("School: ", school, "\nCourse: ", course)

    return render(request, "upload-manually.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    context = generateContext(request)
    return render(request, "register.html", {"form": form, "context": context})


@login_required(login_url="/login")
def profile(request):
    context = generateContext(request)
    return render(request, "profile.html", context)
