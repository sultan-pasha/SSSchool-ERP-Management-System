from django import urls
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls.conf import path
from .models import examReport, homeworkReport, report
from django.contrib.auth.models import User
from students.models import student
from home.models import Lessons
from tasks.models import exam
from django.contrib.auth.decorators import login_required
from coaches.models import coach
from datetime import timedelta, date
# Create your views here.

def homeworkrepfV(request, id):
    if not request.user.is_staff:
        cuser = request.user
        user = User.objects.get(username=cuser)
        lesson = Lessons.objects.get(id = id)
        if request.POST["questions"]==None or request.POST["questions"]=="":
            questionNumber = 0
        else:
            questionNumber = int(request.POST["questions"])
        if request.POST["result"]==None or request.POST["result"]=="" :
            correctNumbers = 0
        else:
            correctNumbers = request.POST["result"]
        if request.POST["wrong"]==None or request.POST["wrong"]=="":
            wrongNumbers = 0
        else:
            wrongNumbers = request.POST["wrong"]
        if request.POST['present']==None or request.POST['present']=="":
            req = 0
        else:
            req = request.POST["present"]
        cstudent = student.objects.get(sinit=user)
        present = int(req[0:-1])
        try : int(wrongNumbers)
        except ValueError:
            wrongNumbers = 0
        if not type(questionNumber) == int or not type(correctNumbers) == int:
            questionNumber = int(questionNumber)
            correctNumbers = int(correctNumbers)
        if not report.objects.filter(user=request.user):
            rep = report(
                user=user,
            )
            rep.save()
        else:
            rep = report.objects.get(user=request.user)
        if not rep.homerport.filter(lesson = lesson).exists():
            rephomework = homeworkReport(
                                user=user,
                                lesson=lesson,
                                asknumber=questionNumber,
                                correctAnswers=correctNumbers,
                                presentage=present,
                                wrongAnswers=wrongNumbers
                                )
            rephomework.save()
            cstudent.finishedHomework.add(lesson)
            rep.homerport.add(rephomework)
            cstudent.shomeworks = (cstudent.shomeworks + rephomework.presentage)
            cstudent.Spercenthomeworks = cstudent.shomeworks / (len(cstudent.finishedHomework.all()))
            cstudent.save()
            messages.success(request, 'تم إرسال اجاباتك بنجاح')
        else:
            messages.info(request, 'عذراً لقد قدمت إجابتك من قبل')
    if request.user.is_staff:
        messages.info(request, "لا يمكنك ارسال هذه المعلومات انت في وضع تجريبي الأن")    
    return redirect("home:lesson", id=id, cid=lesson.catname.id)   

def examrebortfV(request, id):
    if not request.user.is_staff:
        cuser = request.user
        user = User.objects.get(username=cuser)
        cexam = exam.objects.get(id=id)
        if request.POST["questions"]==None or request.POST["questions"]=="":
            questionNumber = 0
        else:
            questionNumber = int(request.POST["questions"])
        if request.POST["result"]==None or request.POST["result"]=="" :
            correctNumbers = 0
        else:
            correctNumbers = request.POST["result"]
        if request.POST["wrong"]==None or request.POST["wrong"]=="":
            wrongNumbers = 0
        else:
            wrongNumbers = request.POST["wrong"]
        if request.POST['present']==None or request.POST['present']=="":
            req = 0
        else:
            req = request.POST["present"]
        cstudent = student.objects.get(sinit=user)
        if req == None or req == "":
            req = 0
            present = int(req)
        else:
            present = int(req)
        try : int(wrongNumbers)
        except ValueError:
            wrongNumbers = 0
        if type(questionNumber) == int and type(correctNumbers) == int:
            questionNumber = int(questionNumber)
            correctNumbers = int(correctNumbers)
        
        if not report.objects.filter(user=request.user):
            rep = report(
                user=user,
            )
            rep.save()
        else:
            rep = report.objects.get(user=request.user)
        if not rep.examReport.filter(exam = cexam).exists():
            repexamreport = examReport(
                                user=user,
                                exam=cexam,
                                asknumber=questionNumber,
                                correctAnswers=correctNumbers,
                                presentage=present,
                                wrongAnswers=wrongNumbers
                                )
            repexamreport.save()
            cstudent.finishExam.add(cexam)
            rep.examReport.add(repexamreport)
            cstudent.sexams = (cstudent.sexams + repexamreport.presentage)
            cstudent.Spercentexams = (cstudent.sexams) / len(cstudent.finishExam.all())
            cstudent.save()
            messages.success(request, 'تم إرسال اجاباتك بنجاح')
        else:
            messages.info(request, 'عذراً لقد قدمت إجابتك من قبل')
    if request.user.is_staff:
        messages.info(request, "لا يمكنك ارسال هذه المعلومات انت في وضع تجريبي الأن")    
    return redirect("task:examscourse", exam.objects.get(id=id).cat.id)

@login_required
def reportV(request):
    endsub = ""
    leceted = ""
    if student.objects.filter(sinit=request.user).exists():
        endsub = student.objects.get(sinit=request.user).SinitDate
        leceted = student.objects.get(sinit= request.user).watchedlecs.all()
    if request.user.is_staff:
        cstudent = student.objects.filter().order_by('-Spercent').first()
        endsub = cstudent.SinitDate
        if report.objects.filter(user = User.objects.get(id=cstudent.sinit.id)).exists():
            cstudent = student.objects.get(sinit=User.objects.get(id=cstudent.sinit.id))
            if homeworkReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id)) and examReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id)).exists( ):
                cstudent.Spercent = (cstudent.Spercentexams + cstudent.Spercenthomeworks) / 2
            else:
                cstudent.Spercent = (cstudent.Spercentexams + cstudent.Spercenthomeworks)
            cstudent.save()
            percent = cstudent.Spercent
            if homeworkReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id)).exists():
                rep = report.objects.get(user = User.objects.get(id=cstudent.sinit.id))
                hrep = homeworkReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id))
            else:
                rep=""
                hrep=""

            if examReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id)).exists( ):
                rep = report.objects.get(user = User.objects.get(id=cstudent.sinit.id))
                erep = examReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id))
            else:
                erep=""
        else:
            rep=""
            hrep=""
            erep=""
            percent=""
        context={
        "cuser": cstudent,
        "rep": rep,
        "hrep": hrep,
        "erep": erep,
        "per": percent,
        "st": student.objects.all().order_by('Spercent')[:6],
        "end": endsub + timedelta(days=30),
        "watched": leceted
        }
    else:
        if report.objects.filter(user = request.user).exists():
            cstudent = student.objects.get(sinit=request.user)
            if homeworkReport.objects.filter(user=request.user) and examReport.objects.filter(user=request.user).exists( ):
                cstudent.Spercent = (cstudent.Spercentexams + cstudent.Spercenthomeworks) / 2
            else:
                cstudent.Spercent = (cstudent.Spercentexams + cstudent.Spercenthomeworks)
            cstudent.save()
            percent = cstudent.Spercent
            if homeworkReport.objects.filter(user=request.user).exists():
                rep = report.objects.get(user = request.user)
                hrep = homeworkReport.objects.filter(user=request.user)
            else:
                rep=""
                hrep=""

            if examReport.objects.filter(user=request.user).exists( ):
                rep = report.objects.get(user = request.user)
                erep = examReport.objects.filter(user=request.user)
            else:
                erep=""
        else:
            rep=""
            hrep=""
            erep=""
            percent=""
    
        context={
        "rep": rep,
        "hrep": hrep,
        "erep": erep,
        "per": percent,
        "st": student.objects.all().order_by('-Spercent')[:5],
        "end": endsub + timedelta(days=30),
        "watched": leceted
        }
    return render(request, "report.html", context)

def prof(request, id):
    endsub = ""
    rpercent = ""
    ruser = ""
    leceted = ""
    cstudent = student.objects.get(id=id)
    if student.objects.filter(id=id).exists():
        endsub = student.objects.get(id=id).SinitDate
        leceted = student.objects.get(id=id).watchedlecs.all()

    if report.objects.filter(user = User.objects.get(id=cstudent.sinit.id)).exists():
        if homeworkReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id)) and examReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id)).exists( ):
            cstudent.Spercent = (cstudent.Spercentexams + cstudent.Spercenthomeworks) / 2
        else:
            cstudent.Spercent = (cstudent.Spercentexams + cstudent.Spercenthomeworks)
        cstudent.save()
        percent = cstudent.Spercent
        if homeworkReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id)).exists():
            rep = report.objects.get(user = User.objects.get(id=cstudent.sinit.id))
            hrep = homeworkReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id))
        else:
            rep=""
            hrep=""

        if examReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id)).exists( ):
            rep = report.objects.get(user = User.objects.get(id=cstudent.sinit.id))
            erep = examReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id))
        else:
            erep=""

    else:
        rep=""
        hrep=""
        erep=""
        percent=0
    # print(User.objects.get(id=cstudent.sinit.id).exists())
    if not request.user.is_staff and report.objects.filter(user=User.objects.get(id=cstudent.sinit.id)).exists():
        if homeworkReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id)) and examReport.objects.filter(user=User.objects.get(id=cstudent.sinit.id)).exists():
            cstudent.Spercent = (cstudent.Spercentexams + cstudent.Spercenthomeworks) / 2
        else:
            cstudent.Spercent = (cstudent.Spercentexams + cstudent.Spercenthomeworks)
        cstudent.save()
    if request.user.is_authenticated:
        if student.objects.filter(sinit=request.user).exists():
            ruser = student.objects.get(sinit=request.user)
            rpercent = student.objects.get(sinit=request.user).Spercent
    context={
    "cuser": cstudent,
    "rep": rep,
    "ruser": ruser,
    "hrep": hrep,
    "erep": erep,
    "per": percent,
    "rper": rpercent,
    "st": student.objects.all().order_by('-Spercent')[:5],
    "end": endsub + timedelta(days=30),
    "watched": leceted
    }
    return render(request, "report.html", context)

def homeworkreportdetailV(request, id):
    if not request.user.is_staff:
        lesson = Lessons.objects.get(id=id)
        rep = homeworkReport.objects.get(lesson = lesson, user=request.user)
    if request.user.is_staff:
        rep = ""
    context={
        "rep": rep
    }
    return render(request, "homeworkreport.html", context)

@login_required
def examreportdetailV(request, id):
    if not request.user.is_staff and examReport.objects.filter(id=id).exists():
        rep = examReport.objects.get(user=request.user, id=id)
    if request.user.is_staff:
        rep = ""
    context={
        "rep": rep
    }
    return render(request, "homeworkreport.html", context)
