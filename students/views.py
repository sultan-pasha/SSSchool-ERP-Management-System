from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as login_auth
from .forms import fstudent
from .models import student
from tasks.models import exam
from home.models import Lessons
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView, LoginView, LogoutView, PasswordResetConfirmView, PasswordResetDoneView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.html import strip_tags
# Create your views here.as_view
def joinV(request):
	name = ""
	nameerr = ""
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		stu = fstudent(request.POST, request.FILES)
		name = request.POST['name']
		if name.split().__len__() > 2:
			if form.is_valid() and stu.is_valid():
				email = request.POST['email']
				form.save()
				stu.save()
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password1')
				cuser = User.objects.get(username = username)
				cuser.email = email
				cuser.save()
				nstu = student.objects.get(Sidnumber=stu.cleaned_data.get('Sidnumber'))
				nstu.sinit = cuser
				nstu.Sfname = name.split()[0]
				nstu.Smname = name.split()[1]
				nstu.Slname = name.split()[2]
				nstu.Sstatus = False
				nstu.save()
				user = authenticate(username=username, password=password)
				if user is not None:
					print(user)
					login_auth(request, user)
					return redirect('/')
				else:
					form = UserCreationForm(request.POST)
					stu = fstudent(request.POST)
			else:
				messages.warning(request, "يوجد خطأ بالبيانات أفحص ادناه")
				form = UserCreationForm(request.POST)
				stu = fstudent(request.POST)
		else:
			form = UserCreationForm(request.POST)
			stu = fstudent(request.POST)
			print(name)
			nameerr = {
				"messg": "يرجي كتابة الأسم الثلاثي للطالب باللغه العربيه",
				"value": name,
			}
			messages.error(request, nameerr["messg"])
	else:
		form=UserCreationForm
		stu=fstudent


	context={
		"form":form,
		"stuf":stu,
		"nameerr":nameerr,
	}
	return render(request, "join.html", context)


class login(LoginView):
	redirect_authenticated_user = True
	template_name='registration/login.html'

class logout(LogoutView):
	template_name='registration/logged_out.html'

class ChangeView(PasswordChangeView):
	template_name='registration/password_change_form.html'
	success_url = reverse_lazy('student:chdone')

class ChangeDoneView(PasswordChangeDoneView):
	template_name='registration/password_change_done.html'

class ResetDone(PasswordResetDoneView):
	template_name='registration/password_reset_done.html'


class Resetconf(PasswordResetConfirmView):
	template_name="registration/change_pass_from_reset.html"
	success_url = reverse_lazy('student:resetcom')

class resetcom(PasswordResetCompleteView):
	template_name="registration/password_reset_complete.html"



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "إستعادة كلمة مرور حسابك علي منصة ساكاد التعليميه"
					email_template_name = "registration/resetemail.html"
					c = {
					"title":subject,
					"email":user.email,
					'domain':request.META['HTTP_HOST'],
					'site_name': 'SACAD platform',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': request.scheme,
					}
					email = render_to_string(email_template_name, c)
					body = strip_tags(email)
					try:
						send_mail(subject, body, 'saskecompany1@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/student/reset_done/")
			else:
				messages.warning(request, "نأسف لم نجد هذا البريد الإلكتروني مسجل لدينا يرجي التحقق من البريد الإلكتروني و إعادة المحاوله")
				return redirect ("/student/password_reset/")
		else:
			messages.warning(request, "نأسف لم نجد هذا البريد الإلكتروني مسجل لدينا يرجي التحقق من البريد الإلكتروني و إعادة المحاوله")
			return redirect ("/student/password_reset/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registration/password_reset_form.html", context={"password_reset_form":password_reset_form})

def profile(request):
	if request.method == "GET":
		if request.user.is_authenticated and not User.objects.get(username=request.user).is_staff:
			cuser = student.objects.get(sinit=request.user)
			if len(cuser.watchedlecs.all()) > 0:
				lecid = cuser.watchedlecs.all().first().id
				if Lessons.objects.filter(id = lecid + 1).exists():
					nextLes = Lessons.objects.get(id = lecid + 1)
				else:
					nextLes = ""
			else:
				nextLes = Lessons.objects.all().last()
			if len(cuser.finishExam.all()) > 0:
				examid = cuser.finishExam.all().last().id
				if exam.objects.filter(id = examid + 1).exists():
					nextexam = exam.objects.get(id = examid + 1)
				else:
					nextexam = ""
			else:
				nextexam = exam.objects.all().first()
		else:
			cuser = ""
		con={
			"st": cuser,
			"nles": nextLes,
			"nex": nextexam
		}
		return render(request=request, template_name='profile/set.html', context=con)
	if request.method == "POST":
		if len(request.POST) < 2:
				nstmimg = request.FILES['stimg']
				cuser = student.objects.get(sinit=request.user)
				cuser.simg = nstmimg
				cuser.save()
		return redirect("/student/profile")


