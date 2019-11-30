from django.urls import path, include 

from .api import RegisterAPI, LoginAPIView
from knox import views as knox_view 

urlpatterns = [
	path('api/auth', include('knox.urls')),
	path('api/auth/register', RegisterAPI.as_view()),
	path('login', LoginAPIView.as_view()),
]