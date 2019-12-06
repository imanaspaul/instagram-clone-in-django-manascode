from django.urls import path, include 
from . views import ProfileView
from .api import RegisterAPI, LoginAPIView
from knox import views as knox_view 

urlpatterns = [
	path('api/auth', include('knox.urls')),
	path('api/auth/register', RegisterAPI.as_view()),
	path('api/auth/login', LoginAPIView.as_view()),
	path('api/auth/profile', ProfileView.as_view()),
]