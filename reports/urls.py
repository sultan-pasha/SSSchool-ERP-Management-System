from django.urls import path
from .views import homeworkrepfV, reportV, homeworkreportdetailV, examrebortfV, examreportdetailV, prof

app_name = "reports"
urlpatterns = [
    path("homework/<int:id>", homeworkrepfV, name="homerf"),
    path("exam/<int:id>", examrebortfV, name="examrf"),
    path("report", reportV, name="report"),
    path("report/homework/<int:id>", homeworkreportdetailV, name="homerv"),
    path("report/exam/<int:id>", examreportdetailV, name="examrv"),
    path("prof/<int:id>", prof, name="prof")
]