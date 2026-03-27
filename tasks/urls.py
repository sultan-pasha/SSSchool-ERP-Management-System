from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import homeworkV, examlistV, examquestV, HomeV
app_name="tasks"

urlpatterns = [
    path("<int:id>", homeworkV, name="homework"),
    path("exams", HomeV, name="exams"),
    path("exams/<int:id>", examlistV, name="examscourse"),
    path("exam/<int:id>", examquestV, name="exam")
]
