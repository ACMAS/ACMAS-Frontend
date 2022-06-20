from django.shortcuts import render
def views.search_index(request):
	html = open('statics/graceful_sticky_jellyfish-html/index.html')
	return httpresponse(html)
# Create your views here.
