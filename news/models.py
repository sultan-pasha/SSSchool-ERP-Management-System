from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class news(models.Model):
    title = models.CharField(_("العنوان"), max_length=256)
    img = models.ImageField(_("صورة الإعلان"), upload_to="./img", blank=True, null=True)
    detail = models.TextField(_("تفاصيل الإعلان"))
    tags= models.CharField(_("كلمة مفتاحيه"), max_length=20, blank=True, null=True)
    pupAt = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(_("عدد مشاهدات الإعلان"), default=0, editable=False)
    likes = models.IntegerField(_("عدد إعجابات بالإعلان"), default=0, editable=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "إعلان"
        verbose_name_plural = "إعلانات"
        ordering = ["-id"]