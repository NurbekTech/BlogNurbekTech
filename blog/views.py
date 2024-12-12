from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from blog.models import Post

# Create your views here.
menu = [{'name': 'Блог', 'url_name': 'blog'},
        {'name': 'Проект', 'url_name': 'project'}]


def index(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
        'menu': menu
    }
    return render(request, 'blog/index.html', context=data)


def blog(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
        'menu': menu
    }
    return render(request, 'blog/blog.html', context=data)


def project(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
        'menu': menu
    }
    return render(request, 'blog/project.html', context=data)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')
