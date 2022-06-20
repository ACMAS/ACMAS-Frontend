from django.shortcuts import render

# Create your views here.
def search(request):
    from django.http import HttpResponse
    html_content = open("templates/reports/search.html")
    return HttpResponse(html_content)
