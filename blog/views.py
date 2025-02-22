from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.

menu = ["Blog", "Project", "About"]


def index(request):
    data = {"title": "NurbekTech!!!", "menu": menu}
    return render(request, "blog/index.html", context=data)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдана</h1>")
