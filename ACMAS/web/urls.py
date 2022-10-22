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
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = (
    [
        path("", views.index, name="index"),
        path("searchByQuestion", views.searchByQuestion, name="searchByQuestion"),
        path("searchByCourse", views.searchByCourse, name="searchByCourse"),
        path("searchResults", views.searchResults, name="searchResults"),
        path("returnQuery", views.returnQuery, name="returnQuery"),
        path("pdfReader", views.pdfReader, name="pdfReader"),
        path("upload-options", views.uploadOptions, name="uploadOptions"),
        path("upload-OCR", views.uploadOCR, name="uploadOCR"),
        path("upload-manually", views.uploadManually, name="uploadManually"),
        path("crop-file/<file_id>/",views.crop_uploaded_file, name="crop-file"),
        path("crop-Img/",views.get_Cropped_Image, name="crop-Img"),
        path("print-Cropped-Imgs/<file_id2>/",views.ocr_cropped_files, name="print-Cropped-Imgs"),
        path("delete-cropped-img/<str:pk>/<str:pk2>/",views.delete_Cropped_Text, name ="delete-cropped-img"),
        path("edit-questin/<str:pk>/<str:pk2>/",views.edit_question, name = "edit-question"),
        path("submit/",views.submit_questions,name="submit")
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
