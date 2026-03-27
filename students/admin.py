from django.contrib import admin
from .models import student
# Register your models here.




class adminstudents(admin.ModelAdmin):
    list_display=['sinit', 'Sfname','Smname','Slname','Spercent']
    # exclude=["shomeworks", "sexams"]
admin.site.register(student, adminstudents)
