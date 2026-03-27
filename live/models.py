from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.

class Live(models.Model):
    Lname = models.CharField(_("اسم اللايف"), max_length=256)
    Lroom = models.CharField(_("رقم الغرفه"), max_length=256)
    Lurl = models.TextField(_("رابط اللايف"))
    Limg = models.ImageField(_("صورة اللايف"), upload_to="live images", blank=True, null=True)
    Linit = models.ForeignKey(User, verbose_name=_("منشيئ اللايف"), on_delete=models.CASCADE)

    def __str__(self):
        return self.Lname + self.Lroom
    class Meta:
        verbose_name = "بث"
        verbose_name_plural = "قائمة البث المباشر"