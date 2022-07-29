from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# from django.core.files.storage import FileSystemStorage
# from django.views.decorators.csrf import csrf_protect
# from django.shortcuts import redirect
# from django.http import HttpResponse


# ACMAS homepage
@csrf_exempt
def index(request):
    return render(request, "index.html")
