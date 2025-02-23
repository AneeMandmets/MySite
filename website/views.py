from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "website/index.html", {
        "title": "HOME"
    })

def projects(request):
    return render(request, "website/projects.html", {
        "title": "PROJECTS"
    })

def contact(request):
    return render(request, "website/contact.html", {
        "title": "CONTACT"
    })

def blog(request):
    return render(request, "website/blog.html", {
        "title": "BLOG"
    })