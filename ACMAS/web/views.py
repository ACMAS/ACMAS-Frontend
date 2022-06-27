from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
	
	return redirect('/web/static/main_page_html/index.html')
def search(request):
	
	return redirect('/web/static/acmas_search_by_course-html/index.html')
