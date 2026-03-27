from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from students.models import student
from home.models import Lessons, catgory
from .models import news
from tasks.models import exam
from coaches.models import coach
from reports.models import report
# Create your views here.

class newsDetailview(DetailView):
    model = news
    template_name='newsdetail.html'
    context_object_name="news"

def newsliked(request, id):
    if news.objects.filter(id=id).exists():
        new = news.objects.get(id=id)
        if student.objects.filter(sinit = request.user).exists():
            if not new in student.objects.get(sinit = request.user).likenews.all():
                student.objects.get(sinit = request.user).likenews.add(new)
                likes = new.likes
                new.likes = likes + 1
                new.save()
            else:
                student.objects.get(sinit = request.user).likenews.remove(new)
                likes = new.likes
                print(likes)
                new.likes = new.likes - 1
                new.save()
    return redirect("news:news")
@login_required
def newslistview(request):
    cats = catgory.objects.all()
    newslist = news.objects.all()
    rep= []
    nextexam = []
    newexam = []
    nextLes = []
    newles = []
    nwork = []
    newnwork = []
    if not request.user.is_staff:
        if not student.objects.get(sinit = request.user).Sstatus or len(student.objects.get(sinit = request.user).Scourses.all()) == 0:
            return redirect("/coaches")
        else:
            cuser = student.objects.get(sinit=request.user)
            lessons = Lessons.objects.all()
            cats= cuser.Scourses.all().order_by("-Crate")[:3]
            if report.objects.filter(user = request.user).exists():
                rep = report.objects.get(user= request.user)

            if len(nextLes) == 0:
                for cours in cuser.Scourses.all():
                    if cuser.watchedlecs.filter(catname = cours).exists():
                        for i in range(cuser.watchedlecs.filter(catname = cours).last().id + 1, Lessons.objects.filter().order_by('id').last().id + 1):
                            if Lessons.objects.filter(catname = cours, id = i).exists():
                                if not Lessons.objects.get(catname = cours, id = i) in cuser.watchedlecs.all():
                                    newles.append(Lessons.objects.get(catname= cours, id = i))
                                    break
                    else:
                        if Lessons.objects.filter(catname=cours).exists():
                            nextLes.append(Lessons.objects.filter(catname=cours).first())

                if len(nextLes) == 0:
                        nextLes=newles

            if len(nextexam) == 0:
                for cours in cuser.Scourses.all():
                    if cuser.finishExam.filter(cat = cours).exists():
                        for i in range(cuser.finishExam.filter(cat = cours).last().id + 1, exam.objects.filter().order_by('id').last().id + 1):
                            if exam.objects.filter(cat = cours, id = i):
                                newexam.append(exam.objects.get(cat= cours, id = i))
                                break
                    else:
                        if exam.objects.filter(cat=cours).exists():
                            nextexam.append(exam.objects.filter(cat=cours).first())
                if len(nextexam) == 0:
                    nextexam = newexam
            if len(nwork) == 0:
                for cours in cuser.Scourses.all():
                    if cuser.finishedHomework.filter(catname = cours).exists():
                        for i in range(cuser.finishedHomework.filter(catname = cours).last().id + 1, Lessons.objects.filter().order_by('id').last().id + 1):
                            if Lessons.objects.filter(catname = cours, id = i):
                                if not Lessons.objects.get(catname = cours, id = i) in cuser.finishedHomework.all():
                                    newnwork.append(Lessons.objects.get(catname= cours, id = i))
                                    break
                    else:
                        if Lessons.objects.filter(catname=cours).exists():
                            nwork.append(Lessons.objects.filter(catname=cours).first())
                if len(nwork) == 0:
                    nwork = newnwork
            # if len(cuser.finishedHomework.all()) > 0:
            #     for cat in cuser.Scourses.all():
            #         for les in Lessons.objects.filter(catname = cat).order_by("id"):
            #             if les in cuser.finishedHomework.all():
            #                 pass
            #             else:
            #                 nwork = les
            #                 break
            else:
                for cat in cuser.Scourses.all():
                    nwork = Lessons.objects.filter(catname = cat).order_by("id").first()
                    break

    else:
        cuser = student.objects.filter().order_by('-Spercent').first()
        lessons = Lessons.objects.all()
        cats = cuser.Scourses.all().order_by("-Crate")[:3]
        nextLes.append(Lessons.objects.filter().order_by('date').last())
        nextexam.append(exam.objects.filter().order_by("publishAt").last())
        nwork = nextLes
        if report.objects.filter(user = cuser.sinit).exists():
            rep = report.objects.get(user= cuser.sinit)
    
    context={
        "nles": nextLes,
        "nex": nextexam,
        "news":newslist,
        "all" : lessons,
        "cats":cats,
        "co": coach.objects.all().order_by('Crate')[:5],
        "rep": rep,
        "nwork": nwork
    }
    return render(request, "index.html", context)

