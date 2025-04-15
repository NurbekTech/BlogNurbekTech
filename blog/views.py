from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

menu = ["Главная", "Блог", "О нас"]


def home(request):
    data = {"title": "Негізгі бет", "menu": menu}
    return render(request, "blog/index.html", context=data)


def about(request):
    data = {"title": "О нас", "menu": menu}
    return render(request, "blog/about.html", context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Оңдай бет жоқ</h1>")
