from django.shortcuts import redirect, render


def index(request):
    # return redirect('/web/static/index.html')
    return render(request, 'index.html')


def searchByQuestion(request):
    # return redirect('web/static/search-by-question.html')
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
