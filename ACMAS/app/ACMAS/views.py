from django.shortcuts import render


# ACMAS homepage
def index(request):
    return render(request, "../static/index.html")
