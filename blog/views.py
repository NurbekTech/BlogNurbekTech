from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from blog.models import *

# Create your views here.
menu = ["Home", "Blog", "About"]


def home(request):
    posts = Post.objects.all()
    return render(
        request, "blog/home.html", {"menu": menu, "title": "Home", "posts": posts}
    )


def about(request):
    return render(request, "blog/about.html", {"menu": menu, "title": "About"})


def custom_404(request, exception):
    return HttpResponseNotFound("Page Not Found")
