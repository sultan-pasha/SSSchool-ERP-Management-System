from django.forms import ModelForm
from .models import student
from django.contrib.auth.models import User

class fstudent(ModelForm):
    class Meta:
        model = student
        fields = '__all__'
        exclude = ['sinit', 'Sstatus', 'finishedHomework', 'finishExam', 'Spercent', 'Spercenthomeworks', 'Spercentexams', 'shomeworks', 'sexams', 'watchedlecs', 'points', 'Scourses', 'Sphone', 'simg', 'Sfname', 'Smname', 'Slname']