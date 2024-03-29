"""ACMAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = (
    [
        path("", views.index, name="index"),
        path("searchByQuestion", views.searchByQuestion, name="searchByQuestion"),
        path("searchByCourse", views.searchByCourse, name="searchByCourse"),
        path("searchResults", views.searchResults, name="searchResults"),
        path("returnQuery", views.returnQuery, name="returnQuery"),
        path("pdfReader", views.pdfReader, name="pdfReader"),
        path("upload-file", views.uploadFile, name="uploadFile"),
        path("upload-manually", views.uploadManually, name="uploadManually"),
        path("sitemap.xml", views.sitemap, name="sitemap"),
        path("favicon.ico", views.favicon, name="favicon"),
        path("robots.txt", views.robots, name="robots"),
        path("register", views.register, name="register"),
        path("", include("django.contrib.auth.urls")),
        path("profile", views.profile, name="profile"),
        path("password/", auth_views.PasswordChangeView.as_view()),
        path("password/done/", auth_views.PasswordChangeDoneView.as_view()),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
