from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from blog.models import Post

# Create your views here.
menu = ['Блог', 'Проекты']


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'title': 'Django', 'menu': menu, 'posts': posts})


def about(request):
    return render(request, 'blog/about.html', {'title': 'Django', 'menu': menu})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')
