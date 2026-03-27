from django.urls import path
from .views import coachesV, coachV, orderV, orderconfV, approveconfV, ordersent
app_name = "coaches"
urlpatterns = [
    path('',coachesV ,name="coaches"),
    path("coach/<int:id>", coachV, name="coach"),
    path("order/<int:CCid>/<int:Cid>", orderV, name="order"),
    path("Confirmorder/<int:Sid>/<int:CCid>/<int:Cid>", orderconfV, name="orderconf"),
    path("sent/", ordersent.as_view(), name="ordersent"),
    path("approve/<int:Sid>/<int:CCid>", approveconfV, name="approveorder"),
]