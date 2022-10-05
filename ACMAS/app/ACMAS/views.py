# IDK why I needed to add this...

from django.shortcuts import render


# ACMAS homepage
def index(request):
    return render(request, "index.html")
