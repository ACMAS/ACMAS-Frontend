# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse


@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)


# the reverse_lazy to redirect the user to login page
class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')
