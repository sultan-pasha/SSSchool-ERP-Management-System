from typing import List
from django.db import models
from django.shortcuts import render
from home.views import lessonv
from students.models import student
from .models import task, exam
from home.models import Lessons, catgory
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def homeworkV(request, id):
    if not request.user.is_staff:
        cuser = User.objects.get(username=request.user)
        lesson = Lessons.objects.get(id=id)
        cstudent = student.objects.get(sinit = cuser)
        finishHomeWork = cstudent.finishedHomework.filter(id=id)
        ask = task.objects.filter(lesson=lesson)

        context={
            "ask":ask,
            "les":lesson,
            "flesh":finishHomeWork
        }
    if request.user.is_staff:
        lesson = Lessons.objects.get(id=id)
        ask = task.objects.filter(lesson=lesson)
        context={
            "ask":ask,
            "les":lesson,
        }
    return render(request, "homeworks.html", context)


# class examlistV(ListView):
#     model= exam
#     template_name = "exams.html"
#     context_object_name = "exams"


@login_required
def HomeV(request):
    context={
        "cats":catgory.objects.all(),
        "all": Lessons.objects.all()
    }
    return render(request, "exams.html", context)


def examlistV(request, id):
    cuser = student.objects.get(sinit = request.user)
    cat = catgory.objects.get(id = id)
    exams = exam.objects.filter(cat=cat)
    
    context= {
        "exams": exams,
        "cat": cat,
        "cats": catgory.objects.all(),
        "all": Lessons.objects.all()
    }
    return render(request, "exams.html", context)

@login_required
def examquestV(request, id):
    if not request.user.is_staff:
        cstudent = student.objects.get(sinit=request.user)
        guid = exam.objects.get(id = id)
        examquest = task.objects.filter(exam=guid)
        finish = cstudent.finishExam.filter(title=guid)
        if not cstudent.finishExam.filter(title=guid).exists():
            views = guid.views + 1
            guid.views = views
            guid.save()
        else:
            pass
    if request.user.is_staff:
        guid = exam.objects.get(id = id)
        examquest = task.objects.filter(exam=guid)
        finish=""
    context = {
        "quest":examquest,
        "exam":guid,
        "finish":finish
    }
    return render(request, "exam.html", context)
