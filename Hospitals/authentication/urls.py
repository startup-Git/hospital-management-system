# Import necessary modules
from django.contrib import admin # Django admin module
from django.urls import path	 # URL routing
from authentication.views import * # Import views from the authentication app

# Define URL patterns
urlpatterns = [
	path('login/', login_page, name='login_page'), # Login page
	path('register/', register_page, name='register'), # Registration page
]
