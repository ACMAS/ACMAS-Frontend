from django.shortcuts import render, redirect
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from .form import User
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse


@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)


# for register page
def register(request):
    if request.POST == "POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            messages.success(request, "Your created your Account!")
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }
    return render(request, "login.html", context)
