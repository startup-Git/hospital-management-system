# Import necessary modules
from django.contrib import admin 
from django.urls import path	 
from authentication.views import *
from django.contrib.auth import views as auth_views

# Define URL patterns
urlpatterns = [
	path('login/', login_page, name='login_page'), 
	path('register/', register_page, name='register'), 
	path('logout/', logout_page, name='logout'),
	path('password/',auth_views.PasswordChangeView.as_view(template_name='authentication/change_password.html')),
]
