from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class student(models.Model):
    def upprofimg(self, filename):
        name = self.sinit
        if len(filename.split('.')) > 0:
            extension = filename.split('.')[-1]
        return ('students/img/%s.%s' %(self.sinit, extension))
    Sstatus = models.BooleanField(_("حالة الطالب"), default=False)
    Sphone = PhoneNumberField(_("واتساب الطالب"), blank=True)
    Sidnumber = models.PositiveBigIntegerField(_("الرقم القومي"), unique=True)
    sinit = models.OneToOneField(User,verbose_name= _("المستخدم"), on_delete=models.CASCADE, blank=True, null=True)
    Sfname = models.CharField(_("الاسم الاول "), max_length=50, null=True, blank=True)
    Smname = models.CharField(_("الاب"), max_length=50, null=True, blank=True)
    Slname = models.CharField(_("الجد"), max_length=50, null=True, blank=True)
    likenews = models.ManyToManyField("news.news", verbose_name=_("الأخبار المعجب بها"), editable=False)
#    Sidgroup = models.CharField(_("رقم المجموعه"), null=True, blank=True, max_length=5)
    Spercent = models.IntegerField(_("نسبة الطالب "), default=0)
    Spercenthomeworks = models.IntegerField(_("نسبة حل الواجبات"), default=0)
    Spercentexams = models.IntegerField(_("نسبة حل الامتحانات"), default=0)
    shomeworks = models.IntegerField(_(" حل الواجبات"), default=0)
    sexams = models.IntegerField(_(" حل الامتحانات"), default=0)
    finishedHomework = models.ManyToManyField("home.Lessons", verbose_name=_("الواجبات التي تم ارسالها"), related_name='homework', blank=True)
    finishExam = models.ManyToManyField("tasks.exam", verbose_name=_("الإمتحانات التي تم ارسالها"), blank=True)
    watchedlecs = models.ManyToManyField('home.lessons', verbose_name=_("المحاضرات المنتهيه"), related_name='wathedlecs', blank=True)
    Scourses = models.ManyToManyField("home.catgory", verbose_name=_("كورسات الطالب"), related_name='Scourses', blank=True)
    points = models.BigIntegerField(_("النقاط"), default=10)
    simg = models.ImageField(_("صورة الطالب"), upload_to=upprofimg, max_length=None, blank=True, null=True)
    SinitDate = models.DateField(_("تاريخ الإشتراك"), auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return f'اسم الطالب:{self.Sfname} {self.Smname} {self.Slname}'
    class Meta:
        verbose_name = "الطالب"
        verbose_name_plural = "الطلاب"
