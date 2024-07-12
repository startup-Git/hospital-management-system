# Import necessary modules
from django.contrib import admin 
from django.urls import path	 
from authentication.views import *
from django.contrib.auth import views as auth_views



# Define URL patterns
urlpatterns = [
    path('dashboard/', Dashboard, name='dashboard'),
    path("profile/", profile, name="profile"),
    path("setting/", Setting, name="setting"),
	path('login/', login_page, name='login'), 
	path('register/', register_page, name='register'), 
	path('logout/', logout_page, name='logout'),
 
	# password change url
	path('password-change/', PasswordChangeView.as_view(), name='password_change'),
	path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='authentication/password_change_done.html'), name='password_change_done'),
 
	# password reset url
 	path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
  
]
