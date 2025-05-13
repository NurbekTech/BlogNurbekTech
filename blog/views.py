from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def home(request):
    return HttpResponse("Hello, Django!")


def custom_404(request, exception):
    return HttpResponseNotFound("Page Not Found")
