from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	html = open('web/index.html')
	return HttpResponse(html)
def search(request):
	
	return HttpResponse(open('web/statics/graceful_sticky_jellyfish-html/index.html'))