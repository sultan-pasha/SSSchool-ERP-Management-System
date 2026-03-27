from django.contrib import admin
from .models import homeworkReport, report, examReport
# Register your models here.
admin.site.register(report)
admin.site.register(homeworkReport)
admin.site.register(examReport)





# class adminhomeworkreport(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         return {}
# admin.site.register(homeworkReport, adminhomeworkreport)


# class adminexamreport(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         return {}
# admin.site.register(examReport, adminexamreport)
