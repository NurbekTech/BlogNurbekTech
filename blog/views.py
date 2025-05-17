from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from blog.models import *

# Create your views here.
menu = [
    {"title": "Blog", "url_name": "blog"},
    {"title": "About", "url_name": "about"},
]


def home(request):
    posts = Post.objects.all()
    data = {"menu": menu, "posts": posts, "title": "Home"}
    return render(request, "blog/home.html", context=data)


def blog(request):
    return HttpResponse("Blog")


def about(request):
    return render(request, "blog/about.html", {"menu": menu, "title": "About"})


def custom_404(request, exception):
    return HttpResponseNotFound("Page Not Found")
