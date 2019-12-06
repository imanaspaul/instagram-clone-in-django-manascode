from django.urls import path, include 
from . views import ProfileView, ExampleView
from .api import RegisterAPI, LoginAPIView
from knox import views as knox_view 

urlpatterns = [
	path('api/auth', include('knox.urls')),
	path('api/auth/register', RegisterAPI.as_view()),
	path('api/auth/login', LoginAPIView.as_view()),
	path('api/auth/profile', ProfileView.as_view()),
	path('api/auth/example', ExampleView.as_view()),
]