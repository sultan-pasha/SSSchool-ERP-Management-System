from django.urls import path
from .views import live, delete_live, livedetail


app_name = "live"

urlpatterns = [
    path('', live, name="live"),
    path('livestart/', livedetail, name="live_det"),
    path('delete/<int:id>', delete_live, name="dlive")
]
