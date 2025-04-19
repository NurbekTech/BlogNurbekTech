from django.urls import path, re_path, register_converter
from blog import views


urlpatterns = [
    path("", views.home, name="home"),
    path("blog/", views.blog, name="blog"),
    path("project/", views.project, name="project"),
    path("about/", views.about, name="about"),
    path("post/<int:post_id>", views.show_post, name="post"),
]
