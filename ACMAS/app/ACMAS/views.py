from django.shortcuts import render


# ACMAS homepage
def index(request):
    return render(request, "../ACMAS_Web/templates/index.html")
