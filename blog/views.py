from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')
