from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, Django!</h1>")


def custom_404_view(request, exception):
    return HttpResponseNotFound("Страница не найдена")
