from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


def index(request):
    return render(request, 'index.html')


@csrf_protect
def searchByQuestion(request):
    question = request.POST.get('question')
    if question is not None and len(question) > 0:
        print(question)
    return render(request, 'search-by-question.html')


def searchByCourse(request):
    return render(request, 'search-by-course.html')


def uploadSearch(request):
    return render(request, 'upload-search.html')


def getQuestionInput(request):
    question = request.GET.get('question')
    if len(question) == 0:
        print("No question input")
    else:
        print(question)
