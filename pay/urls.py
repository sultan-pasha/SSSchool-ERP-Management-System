from django.urls import path
from .views import token
app_name = 'pay'

urlpatterns = [
	path('', token, name='pay'),
]