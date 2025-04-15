from django.urls import path, re_path, register_converter
from blog import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
