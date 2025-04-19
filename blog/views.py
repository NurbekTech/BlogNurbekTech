from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from blog.models import Post, Category

# Create your views here.

menu = [
    {"title": "Блог", "url_name": "blog"},
    {"title": "Проекты", "url_name": "project"},
    {"title": "О нас", "url_name": "about"},
]


def home(request):
    posts = Post.objects.all()
    data = {"title": "Негізгі бет", "menu": menu, "posts": posts}
    return render(request, "blog/index.html", context=data)


def blog(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    data = {"title": "Блог", "menu": menu, "posts": posts, "cats": cats}
    return render(request, "blog/blog.html", context=data)


def project(request):
    return HttpResponse("Project")


def about(request):
    data = {"title": "О нас", "menu": menu}
    return render(request, "blog/about.html", context=data)


def show_post(request, post_id):
    return HttpResponse(f"Post {post_id}")


def show_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    data = {"title": "Блог", "menu": menu, "posts": posts, "cats": cats}
    return render(request, "blog/blog.html", context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Оңдай бет жоқ</h1>")
