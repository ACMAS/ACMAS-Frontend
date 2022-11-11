from django.urls import path
from django.contrib import admin
from .views import Register
urlpatterns = [
    path("register/", Register.as_view(), name="register"),
]
