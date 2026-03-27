from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Lessons(models.Model):
    levels=[
        ("سهل", "سهل"),
        ("متوسط", "متوسط"),
        ("صعب", "صعب"),
    ]
    class Meta:
        verbose_name = "المحاضره"
        verbose_name_plural = "المحاضرات"
        ordering = ['-date']


    def upleson(self, filename):
        name = filename.split(".")
        return "lessons/%s.%s" %(self.name, name[-1])


    def uplesonimg(self, filename):
        name = filename.split(".")
        return "thumbnails/leson/%s.%s" %(self.name, name[-1])

    name = models.CharField(_("اسم الحصه"),max_length=256)
    catname = models.ForeignKey("home.catgory", verbose_name=_("يتبع"), on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateField(_("تاريخ الحصه"), auto_now=True)
    video = models.FileField(_("الحصه"), upload_to=upleson, blank=True, null=True)
    limg = models.ImageField(_("صورة مصغره للحلقه"),upload_to=uplesonimg, null=True, blank=True)
    LYoutube = models.CharField(_("لينك الحلقه من اليوتيوب"), max_length=255, blank=True, null=True)
    Lviews = models.IntegerField(_("عدد مشاهدات الدرس"), default=0, editable=False)
    Llevel = models.CharField(_("مستوي المحاضره"), choices=levels, max_length=10, default="متوسط", blank=False)
    LHlevel = models.CharField(_("مستوي الواجبات"), choices=levels, max_length=10, default="متوسط", blank=False)
    def __str__(self):
        return f'{self.id}- {self.name}, من فرع {self.catname}'

    def get_absolute_url(self):
        return reverse("home:lesson", kwargs={"id": self.id})
    
class catgory(models.Model):
    rates =[
    ("⭐", "⭐"),
    ("⭐⭐", "⭐⭐"),
    ("⭐⭐⭐", "⭐⭐⭐"),
    ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
    ]
    def upcatimg(self, filename):
        name = filename.split(".")
        return "thumbnails/categories/%s.%s" %(self.name, name[-1])
    name = models.CharField(_("اسم الكورس"), max_length=50)
    cimage = models.ImageField(_("لوجو الكورس ان وجد"),upload_to=upcatimg, null=True, blank=True)
    CCoach = models.ForeignKey("coaches.Coach", verbose_name=_("مدرب الكورس"), on_delete=models.CASCADE, blank=True, null=True)
    Cprice = models.IntegerField(_("قيمة الإشتراك شهري"), blank=True, null=True)
    Crate = models.CharField(_('مستوي المدرب'), choices= rates, default="⭐⭐⭐⭐⭐", max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "الكورس"
        verbose_name_plural = "الكورسات"
        
    def get_absolute_url(self):
        return reverse("home:lessons", kwargs={"id": self.id})
    