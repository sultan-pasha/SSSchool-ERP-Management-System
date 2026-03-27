from django.contrib import admin
from .models import task, exam
from django.utils.html import format_html
# Register your models here.
admin.site.register(exam)

@admin.register(task)
class taskadmin(admin.ModelAdmin):
    list_display = ('id','quest','questimg', 'answer', 'lesson', 'exam')
    