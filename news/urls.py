from django.urls import path
from .views import newslistview, newsDetailview, newsliked
app_name = "news"
urlpatterns = [
    path('', newslistview, name="news"),
    path('news/<int:pk>', newsDetailview.as_view(), name="newdet"),
    path('news/like/<int:id>', newsliked, name="likenews")
]