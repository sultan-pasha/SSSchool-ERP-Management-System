from django.shortcuts import render
from .models import Lessons, catgory
from django.contrib.auth.decorators import login_required
from students.models import student

# Create your views here.

@login_required
def HomeV(request):
    context={
        "cats":catgory.objects.all(),
        "all": Lessons.objects.all()
    }
    return render(request, "cats.html", context)


@login_required
def lessonv(request, id):
    if not request.user.is_staff:
        cuser = student.objects.get(sinit=request.user)
        cat = catgory.objects.get(id=id)
        lessons = Lessons.objects.filter(catname=cat)
    if request.user.is_staff:
        cat = catgory.objects.get(id=id)
        lessons = Lessons.objects.filter(catname = cat)
    
    context={
        "les":lessons,
        "cat":cat,
        "all": Lessons.objects.all(),
        "cats": catgory.objects.all()
    }
    return render(request, "lessons.html", context)

@login_required
def lessondetail(request, id, cid):
    lesvisit = ""
    if catgory.objects.filter(id=cid).exists():
        cat = catgory.objects.get(id=cid)
    if not request.user.is_staff:
        cuser = student.objects.get(sinit=request.user)
        if cuser.Scourses.filter(id=cid).exists():
            if not cuser.watchedlecs.filter(id=id).exists():
                if Lessons.objects.filter(id = id, catname=cuser.Scourses.get(id=cid)).exists():
                    lesvisit = Lessons.objects.get(id = id, catname=cuser.Scourses.get(id=cid))
                    
                if lesvisit in cuser.watchedlecs.all():
                    lesvisit = Lessons.objects.get(id = id)
                    
                else:
                    if cuser.points >= 10:
                        cuser.points = cuser.points - 10
                        cuser.watchedlecs.add(lesvisit)
                        lviews = lesvisit.Lviews + 1
                        lesvisit.Lviews = lviews
                        lesvisit.save()
                        cuser.save()
                    else:
                        if lesvisit:
                            if lesvisit.catname in cuser.Scourses.all():
                                cuser.watchedlecs.add(lesvisit)
                                lviews = lesvisit.Lviews + 1
                                lesvisit.Lviews = lviews
                                lesvisit.save()
                                cuser.save()
                            else:
                                lesvisit = []
            else:
                lesvisit = Lessons.objects.get(id = id)
    else:
        lesvisit = Lessons.objects.get(id = id)
        cat = Lessons.objects.get(id = id).catname
    # if not request.user.is_staff:
    #     cuser = student.objects.get(sinit=request.user)
    #     if Lessons.objects.filter(id = id).exists:
    #         lesvisit = Lessons.objects.get(id = id)
    #     if cuser.points < 10 and lesvisit.catname in cuser.Scourses.all() :
    #         if lesvisit in cuser.watchedlecs.all():
    #             lesvisit = lesvisit
    #         else:
    #             cuser.watchedlecs.add(lesvisit)
    #             cuser.save()
    #     else:
    #         lesvisit = []
    #         cat = Lessons.objects.get(id = id).catname
    #     if cuser.points >= 10 and lesvisit not in cuser.watchedlecs.all():
    #         lesvisit = Lessons.objects.get(id = id)
    #         cuser.watchedlecs.add(lesvisit)
    #         cuser.points = cuser.points - 10
    #         cuser.save()
    # else:
    #     lesvisit = Lessons.objects.get(id = id)
    #     cat = Lessons.objects.get(id = id).catname
    context={
        "lesson": lesvisit,
        "cat": cat
    }
    return render(request, "lesson.html", context)


# @login_required
# def lecsv(request):
#     if not request.user.is_staff:
#         cuser = student.objects.get(sinit=request.user)
#         lessons = Lessons.objects.all()
#     if request.user.is_staff:
#         lessons = Lessons.objects.all()
#     context={
#         "all" : lessons
#     }
#     return render(request, "lecs.html", context)


def mycoursesV(request):
    st = student.objects.get(sinit=request.user)
    courses = st.Scourses.all()
    context= {
        "courses": courses
    }
    return render(request, "mycourses.html", context)

def search(rquest):
    pass

def handel400(request, exception):
    return render(request, "400.html", status=400)

def handel403(request, exception):
    return render(request, "403.html", status=403)

def handel404(request, exception):
    return render(request, "404.html", status=404)

def handel500(request, exception):
    return render(request, "500.html", status=500)