
from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home),
    path('', views.home),
    path('graphiques.html', views.graphiques)


]