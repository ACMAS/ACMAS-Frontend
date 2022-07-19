from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.shortcuts import redirect
from django.db.models.query import EmptyQuerySet
from .models import UploadedFile
# from django.http import HttpResponse


# Create your views here.
@csrf_exempt
def index(request):
    return redirect("static/index.html")


@csrf_protect
def searchByQuestion(request):
    question = request.POST.get("question")
    if question is not None and len(question) > 0:
        print("Manual question: ", question)
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
        files = UploadedFile.objects.filter(flag=(school+"|"+course))
        if( files.exists() ):
            return render(request, "search-results.html", {'files':files})
    return render(request, "search-results.html")

@csrf_protect
#@xframe_options_exempt
def pdfReader(request):
    url = request.GET.get('url')
    url = "../static/" + url
    return render(request, "pdf-reader.html", {"url": url})

@csrf_protect
def uploadSearch(request):
    """
    question = request.POST.get("question")
    if question is not None and len(question) > 0:
        print("question: ", question)
    school = request.POST.get("school")
    course = request.POST.get("course")
    if (
        school is not None
        and course is not None
        and len(school) > 0
        and len(course) > 0
    ):
        file = UploadedFile(filename="IPR-CSCI2300-HW4.pdf", file_dir="../static/IPR-CSCI2300-HW4.pdf", date_uploaded="today", flag=(school+"|"+course))
        file.save()
    """
    return render(request, "upload-search.html")
