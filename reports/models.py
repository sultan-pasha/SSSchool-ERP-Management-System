from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
class report(models.Model):
    user = models.ForeignKey("auth.User", verbose_name=_("الطالب"), on_delete=models.CASCADE, null=True, blank=True)
    homerport = models.ManyToManyField("homeworkReport", verbose_name=_("واجبات الطالب"), blank=True)
    examReport = models.ManyToManyField("examReport", verbose_name=_("امتحانات الطالب"), blank=True)
    
    def __str__(self):
        return f"تقرير {self.user}"
    class Meta:
        verbose_name = "التقرير"
        verbose_name_plural = "التقارير"
class homeworkReport(models.Model):
    user = models.ForeignKey("auth.User", verbose_name=_("الطالب"), on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey("home.Lessons", verbose_name=_("واجب درس"), on_delete=models.CASCADE)
    asknumber = models.IntegerField(_("عدد الاسئله"), null=True, blank=True)
    correctAnswers = models.IntegerField(_("الاجابات الصحيحه"), null=True, blank=True)
    wrongAnswers = models.IntegerField(_("الإجابات الخاطئه"), null=True, blank=True)
    presentage = models.IntegerField(_("النسبه المئويه"),null=True, blank=True,)
    class Meta:
        ordering = ['id']
    def __str__(self):
        return f"تقرير واجب منزلي {self.lesson} للطالب {self.user} "
    class Meta:
        verbose_name = "تقرير واجب"
        verbose_name_plural = "تقاربر الواجب"



class examReport(models.Model):
    user = models.ForeignKey("auth.User", verbose_name=_("الطالب"), on_delete=models.CASCADE, null=True, blank=True)
    exam = models.ForeignKey("tasks.exam", verbose_name=_("امتحان"), on_delete=models.CASCADE, null=True, blank=True)
    asknumber = models.IntegerField(_("عدد الاسئله"), null=True, blank=True)
    correctAnswers = models.IntegerField(_("الاجابات الصحيحه"), null=True, blank=True)
    wrongAnswers = models.IntegerField(_("الإجابات الخاطئه"), null=True, blank=True)
    presentage = models.IntegerField(_("النسبه المئويه"),null=True, blank=True)
    
    class Meta:
        ordering = ['id']
    def __str__(self):
        return f"تقرير {self.exam} للطالب {self.user} "
    
    class Meta:
        verbose_name = "تقرير امتحان"
        verbose_name_plural = "تقارير الامتحانات"
