from django.utils.html import format_html
from django.contrib import admin
from.models import Lessons, catgory
# Register your models here.
admin.site.register(catgory)

class lessonadmin(admin.ModelAdmin):
    list_display = ['id', "name", "video", 'catname', 'date']
admin.site.register(Lessons, lessonadmin)




