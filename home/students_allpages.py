from students.models import student
from django.contrib.auth.models import User
from django.db.models import Q
from home.models import Lessons
from coaches.models import coach
from tasks.models import exam
from django.shortcuts import redirect

def cuser(request):
    if request.user.is_authenticated:
        if not request.user.is_staff:
            currentuser = User.objects.get(username=request.user)
            cstudent = student.objects.get(sinit=currentuser.id)
            if cstudent.sinit == currentuser.id:
                print("pass")
                if cstudent.Sstatus:
                    pass
                else:
                    print("come")
                    return redirect("coaches:coaches")
        if request.user.is_staff:
            currentuser = User.objects.get(username=request.user)
            cstudent=""
    else:
        currentuser=""
        cstudent =""

    context={
        "user":currentuser,
        'cuser':cstudent
    }
    return (context)

def searchV(request):
    les = ""
    st = ""
    ex = ""
    co = ""
    if 'q' in request.GET:
        q = request.GET['q']
        Lquery = Q(Q(name__icontains=q))
        Squery = Q(Q(Sfname__icontains=q) | Q(Smname__icontains=q) | Q(Slname__icontains=q))
        Equery = Q(title__icontains=q)
        Cquery = Q(CName__icontains=q)
        if Lessons.objects.filter(Lquery).exists():
            les = Lessons.objects.filter(Lquery)
        if student.objects.filter(Squery).exists():
            st = student.objects.filter(Squery)
        if exam.objects.filter(Equery).exists():
            ex = exam.objects.filter(Equery)
        if coach.objects.filter(Cquery).exists():
            co = coach.objects.filter(Cquery)
    context = {
        "lessearch":les,
        "stusearch":st,
        "examsearch":ex,
        "cosearch":co,
    }
    return (context)