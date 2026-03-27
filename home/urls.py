from django.urls import path
from .views import HomeV, lessondetail, lessonv, mycoursesV

app_name = "home"
urlpatterns = [
    path('tracks', HomeV, name="home"),
    path('<int:id>', lessonv, name='lessons'),
    path('lesson/<int:id>/<int:cid>', lessondetail, name='lesson'),
    # path("lectures", lecsv, name="all"),
    path('mycourses', mycoursesV, name="mycourses"),
]