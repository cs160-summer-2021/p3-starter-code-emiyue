from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('projects', views.projects, name='projects')
]
