from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog'),
    path('project/', views.project, name='project'),
    path('post/<int:post_id>/', views.show_post, name='post'),
]
