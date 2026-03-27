from django.urls import path, include



from .views import joinV, login, logout, ResetDone, ChangeView, ChangeDoneView, Resetconf, resetcom, password_reset_request, profile


app_name = 'students'
urlpatterns = [
    path("", joinV, name='join'),
    path("login/", login.as_view(), name='login'),
    path("logout/",logout.as_view(),name='logout'),

    path("changepassword/",ChangeView.as_view(),name='change'),
    path("password_change_done/",ChangeDoneView.as_view(),name='chdone'),

    path("password_reset/",password_reset_request,name='reset'),
    path("reset_done/",ResetDone.as_view(),name='resetconf'),
    path("reset_confirm/<uidb64>/<token>",Resetconf.as_view(),name='resetdone'),
    path("reset_complete",resetcom.as_view(),name='resetcom'),
    path("profile",profile,name='prof'),
]
