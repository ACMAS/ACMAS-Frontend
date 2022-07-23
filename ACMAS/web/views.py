from datetime import date

from django.core.files.storage import FileSystemStorage
from django.db.models.query import EmptyQuerySet
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import Question, UploadedFile

# from django.shortcuts import redirect
# from django.http import HttpResponse
# from django.views.decorators.clickjacking import xframe_options_sameorigin


# Create your views here.
@csrf_exempt
def index(request):
    return redirect("static/index.html")


@csrf_protect
def searchByQuestion(request):
    question = request.POST.get("question")
    if question is not None and len(question) > 0:
        print("Manual question:", question)
    elif len(request.FILES) != 0:
        file = request.FILES["fileUpload"]
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
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
        print("Assignment Type:", assignmentType)
        files = UploadedFile.objects.filter(flag=(school + "|" + course))
        if files.exists():
            return render(request, "search-results.html", {"files": files})
    return render(request, "search-results.html")


@csrf_protect
def pdfReader(request):
    url = request.GET.get("url")
    url = "media/" + url
    return render(request, "pdf-reader.html", {"url": url})


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
            db_file = UploadedFile(
                filename=filename,
                file_dir=file_url,
                date_uploaded=date.today(),
                flag=(school + "|" + course)
            )
            db_file.save()
            print(f'FILE "{filename}" uploaded to "{file_url}"\n')
    return render(request, "upload-search.html")
