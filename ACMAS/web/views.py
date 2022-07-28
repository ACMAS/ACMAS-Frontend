from datetime import date

from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
from django.db.models.query import EmptyQuerySet
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import Course, Question, University, UploadedFile
from .python_classes.search import searchFacade

# from django.shortcuts import redirect
# from django.http import HttpResponse
# from django.views.decorators.clickjacking import xframe_options_sameorigin


# Create your views here.
@csrf_exempt
def index(request):
    return redirect("static/index.html")


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


@csrf_exempt
def searchByCourse(request):
    return render(request, "search-by-course.html")


@csrf_exempt
def searchResults(request):

    school = request.POST.get("school")
    course = request.POST.get("course")
    assignmentType = request.POST.get("type")
    files = EmptyQuerySet
    if (
        school is not None
        and course is not None
        and len(school) > 0
        and len(course) > 0
    ):
        print("University:", school)
        print("Course:", course)
        print("Assignment Type:", assignmentType)
        sessionID = request.session._get_or_create_session_key()
        request.session.modified = True
        facade = cache.get(sessionID)
        if facade == None:
            cache.set(sessionID, searchFacade(), 1200)
            facade = cache.get(sessionID)

        files = facade.search(school, course, assignmentType)
        cache.set(sessionID, facade, 1200)

        if files != None:
            return render(request, "search-results.html", {"files": files})
    return render(request, "search-results.html")

@csrf_exempt
def returnQuery(request):

    sessionID = request.session._get_or_create_session_key()
    facade = cache.get(sessionID)

    if facade == None:
        return render(request, "search-by-course.html")
    return render(request, "search-results.html", {"files": facade.getQuery()})

@csrf_protect
def pdfReader(request):

    name = request.GET.get("url")
    sessionID = request.session._get_or_create_session_key()
    facade = cache.get(sessionID)

    if(facade.getQuery() != None):
            print("Reader: courseFiles exists")

    if facade == None or facade.getQuery() == None:
        file = UploadedFile.objects.get(filename=name)
        return render(request, "pdf-reader.html", {"directory": file.file_dir})

    file = facade.getQuery().get(filename=name)
    return render(request, "pdf-reader.html", {"directory": file.file_dir})


@csrf_protect
def uploadSearch(request):
    question = request.POST.get("question")
    answer = request.POST.get("answer")
    if (
        question is not None
        and answer is not None
        and len(question) > 0
        and len(answer) > 0
    ):
        db_question = Question(question=question, Answers=answer, Hash="")
        db_question.save()
        print("Manual question:", question)
        print("Manual answer:", answer)
    elif len(request.FILES) != 0:
        school = request.POST.get("school")
        course = request.POST.get("course")
        file = request.FILES["fileUpload"]
        if (
            school is not None
            and course is not None
            and file is not None
            and len(school) > 0
            and len(course) > 0
        ):
            print("School:", school, "\nCourse:", course)
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_url = fs.url(filename)
            print(filename, file_url, date.today(), (school + "|" + course))
            if not University.objects.filter(name=school).exists():
                uni = University(name=school)
                uni.save()
                print("Created university:", school)
            if not Course.objects.filter(name=course).exists():
                new_course = Course(
                    name=course,
                    university=University.objects.get(name=school),
                )
                new_course.save()
                print("Created course:", course)
            db_file = UploadedFile(
                filename=filename,
                file_dir=file_url,
                course=Course.objects.get(name=course),
                date_uploaded=date.today(),
                flag=("Assignment"),
            )
            db_file.save()
            print(f'FILE "{filename}" uploaded to "{file_url}"\n')
    return render(request, "upload-search.html")
