from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# ACMAS homepage
@csrf_exempt
def index(request):
    return render(request, "index.html")
