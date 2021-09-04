from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners
def index(request):
    return render(request,"index.html")
def analyze(request):
    link=request.POST.get("link")
    if link and link.startswith("https://"):
        s = pyshorteners.Shortener()
        shortened_link=s.tinyurl.short(link)
        params={
            "shortened_link":shortened_link
        }
    else:
        return render(request,"error.html")
    return render(request,"analyze.html",params)
def about(request):
    return render(request,"about.html")