from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	html = open('web/index.html')
	return HttpResponse(html)
