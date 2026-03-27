from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
rates =[
    ("⭐", "⭐"),
    ("⭐⭐", "⭐⭐"),
    ("⭐⭐⭐", "⭐⭐⭐"),
    ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
]
class coach(models.Model):
    def Cimage_Up(self, filename):
        name = self.CName
        if len(filename.split('.')) > 0:
            extension = filename.split('.')[-1]
            return ('coaches/img/%s.%s' %(self.sinit, extension))
    User = models.OneToOneField(User, verbose_name=_("المستخدم"), on_delete=models.CASCADE)
    CName = models.CharField(_("اسم المدرب"), max_length=50)
    CPhone = PhoneNumberField(_("رقم المدرب"), blank=True)
    Cemail = models.EmailField(_("بريد المدرب"), max_length=254)
    Crate = models.CharField(_('مستوي المدرب'), choices= rates, default="⭐⭐⭐⭐⭐", max_length=50)
    Cimg = models.ImageField(_("الصوره الشخصيه"), upload_to=Cimage_Up, max_length=None, blank=True, null=True)
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'المدرب'
        verbose_name_plural = 'المدربين'
    def __str__(self):
        return self.CName
    