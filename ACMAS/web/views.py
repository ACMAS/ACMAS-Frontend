from django.shortcuts import render
def views.search_index(request):
	html = open('statics/search_index.html')
	return httpresponse(html)
# Create your views here.
