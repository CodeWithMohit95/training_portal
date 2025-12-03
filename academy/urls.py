from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('academy/courses/', courses, name="courses"),
    path('academy/trainers/', trainers, name="trainers"),
    path('academy/students/', students, name="students"),
]
