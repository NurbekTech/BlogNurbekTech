from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog'),
    path('project/', views.project, name='project'),
]
