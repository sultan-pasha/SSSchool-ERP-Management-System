from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from students.models import student
from .models import Live

# Create your views here.
@login_required
def live(request):
    if request.method == "GET":
        if request.user.is_staff:
            cuser = request.user
            live = ""
        else:
            cuser = student.objects.get(sinit = request.user)
            live = Live.objects.all()
        context = {
            "cuser": cuser,
            "live" : live
        }
        return render(request, 'live.html', context)
    else:
        if not Live.objects.filter(Linit=request.user):
            if request.POST['lname'] and request.POST['lurl'] and request.FILES["limg"] and request.POST['lroomid']:
                initlive = Live()
                initlive.Lname = request.POST['lname']
                initlive.Lurl = request.POST['lurl']
                initlive.Limg = request.FILES["limg"]
                initlive.Lroom = request.POST['lroomid']
                initlive.Linit = request.user
                initlive.save()
                newlive = Live.objects.filter(Linit = request.user).last()
                urllive = newlive.Lurl
        else:
            if request.POST['lname'] and request.POST['lurl'] and request.FILES["limg"] and request.POST['lroomid']:
                initlive = Live.objects.get(Linit=request.user)
                initlive.Lname = request.POST['lname']
                initlive.Lurl = request.POST['lurl']
                initlive.Limg = request.FILES["limg"]
                initlive.Lroom = request.POST['lroomid']
                initlive.Linit = request.user
                initlive.save()
                newlive = Live.objects.filter(Linit = request.user).last()
                urllive = newlive.Lurl
        return redirect("/" + newlive.Lurl)
    return redirect("/live")

def livedetail(request):
    if request.method == "GET":
        room = request.GET["roomID"]
        if Live.objects.filter(Lroom=room).exists():
            if request.user.is_staff:
                cuser = request.user
            else:
                cuser = student.objects.get(sinit = request.user)
            context = {
                "cuser": cuser,
            }
            return render(request, 'live_detail.html', context)
        else:
            return redirect("/")
            

def delete_live(request, id):
    if Live.objects.filter(Lroom=id).exists() and Live.objects.filter(Linit=request.user):
        dlive = Live.objects.get(Lroom=id)
        dlive.delete()
    return redirect("/")


