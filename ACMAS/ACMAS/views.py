from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse


# ACMAS homepage
@csrf_exempt
def index(request):
    return render(request, "index.html")

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')
