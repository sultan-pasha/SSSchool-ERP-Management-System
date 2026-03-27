from django.shortcuts import render, redirect, get_object_or_404
from .models import coach
from home.models import catgory 
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.http import HttpResponse
from students.models import student
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.
def coachesV(request):
    coaches = {
        "coaches":coach.objects.all(),
        "cats": catgory.objects.all()
    }
    return render(request, "coaches.html", coaches)

def coachV(request, id):
    Ccoach = {
        "coach": get_object_or_404(coach, id=id),
        "cats": catgory.objects.filter(CCoach=coach.objects.get(id=id))
    }
    return render(request, "coach.html", Ccoach)


def orderV(request, Cid, CCid):
    email_template_name = "newstudentmail.html"
    subject = "اشتراك طالب جديد بكورس %s" %(catgory.objects.get(id=CCid))
    c = {
        "titile":subject,
        'domain': request.META['HTTP_HOST'],
        'site_name': 'SACAD platform',
        "user": request.user,
        'protocol': request.scheme,
        "coach": coach.objects.get(id=Cid),
        "cat": catgory.objects.get(id=CCid),
        "st": student.objects.get(sinit=request.user)
        }
    email = render_to_string(email_template_name, c)
    try:
        send_mail(subject, email, 'saskecompany1@gmail.com' , [coach.objects.get(id=Cid).Cemail], fail_silently=False)    
    except BadHeaderError:
        print("done")
        return HttpResponse('Invalid header found.')
    return redirect("/coaches/sent/")

class ordersent(TemplateView):
    template_name = "ordersent.html"

@login_required()
def orderconfV(request,Sid, Cid, CCid):
    if not request.user == coach.objects.get(id=Cid).User:
        notallowed = "يرجي التسجيل بحساب المدرب صاحب الكورس وشكراً لكم"
    else:
        notallowed = []
    context={
        "st": student.objects.get(sinit=User.objects.get(id=Sid)),
        "cat": catgory.objects.get(id=CCid),
        "coach": coach.objects.get(id=Cid),
        "notallowed":notallowed
    }
    return render(request, "orderconfirmation.html", context)

def approveconfV(request, Sid, CCid):
    st = student.objects.get(id=Sid)
    if not st.Sstatus:
        st.Sstatus = True
    cat = catgory.objects.get(id=CCid)
    st.Scourses.add(cat)
    st.save()
    return redirect("/admin/students/student/%s/change" %(Sid))


