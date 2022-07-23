from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# from django.core.files.storage import FileSystemStorage
# from django.views.decorators.csrf import csrf_protect
# from django.shortcuts import redirect
# from django.http import HttpResponse


# Create your views here.
@csrf_exempt
def index(request):
    return render(request, "index.html")


"""
@csrf_protect
def searchByQuestion(request):
    question = request.POST.get("question")
    if question is not None and len(question) > 0:
        print("Manual question: ", question)
    elif len(request.FILES) != 0:
        file = request.FILES["fileUpload"]
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        print(f'FILE "{filename}" uploaded to "{file_url}"\n')
    return render(request, "search-by-question.html")


@csrf_protect
def searchByCourse(request):
    school = request.POST.get("school")
    course = request.POST.get("course")
    assignmentType = request.POST.get("type")
    if (
        school is not None
        and course is not None
        and len(school) > 0
        and len(course) > 0
    ):
        print(
            "School: ",
            school,
            "\nCourse: ",
            course,
            "\nAssignment type: ",
            assignmentType,
        )
    return render(request, "search-by-course.html")


@csrf_protect
def uploadSearch(request):
    question = request.POST.get("question")
    if question is not None and len(question) > 0:
        print("Manual question: ", question)
    school = request.POST.get("school")
    course = request.POST.get("course")
    if (
        school is not None
        and course is not None
        and len(school) > 0
        and len(course) > 0
    ):
        print("School: ", school, "\nCourse: ", course)
    return render(request, "upload-search.html")


"""
