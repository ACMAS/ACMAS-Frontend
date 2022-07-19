from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Create your views here.
@csrf_exempt
def index(request):
    return render(request, "index.html")


@csrf_protect
def searchByQuestion(request):
    question = request.POST.get("question")
    if question is not None and len(question) > 0:
        print("Manual question: ", question)
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
