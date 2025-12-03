from django.shortcuts import render
from .models import Course, Trainer, Student

def home(request):
    context = {
        "total_courses": Course.objects.all().count(),
        "total_trainers": Trainer.objects.all().count(),
        "total_students": Student.objects.all().count(),
    }
    return render(request, "home.html", context)


def courses(request):
    return render(request, "courses.html", {
        "courses": Course.objects.all()
    })


def trainers(request):
    return render(request, "trainers.html", {
        "trainers": Trainer.objects.all()
    })


def students(request):
    return render(request, "students.html", {
        "students": Student.objects.all()
    })
