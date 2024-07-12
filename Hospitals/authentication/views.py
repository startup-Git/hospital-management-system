# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views import generic
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def register_page(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = User.objects.filter(username=username)
		
		if user.exists():
			messages.info(request, "Username already taken!")
			return redirect('/register/')
		
		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username
		)
		
		user.set_password(password)
		user.save()
		
		messages.info(request, "Account created Successfully!")
		return redirect('/register/')
	
	return render(request, 'registration.html')

def login_page(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		if not User.objects.filter(username=username).exists():
			messages.error(request, 'Invalid Username')
			return redirect('/login/')
		
		user = authenticate(username=username, password=password)
		
		if user is None:
			messages.error(request, "Invalid Password")
			return redirect('/login/')
		else:
			login(request, user)
			return redirect('/')
	
	return render(request, 'login.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'logout Successfully')
    return redirect('index')


def Dashboard(request):
    return render(request, 'Dashboard/dashboard.html')

def profile(request):
    return render(request, 'Dashboard/dashboard.html')

def Setting(request):
    pass


class PasswordChangeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'authentication/change_password.html'
    success_url = reverse_lazy("password_change_done")
    
    def post(self, request, *args, **kwargs):
        
        old_password: str = request.POST.get('old_password')
        new_password1: str = request.POST.get('new_password1')
        new_password2: str = request.POST.get('new_password2')
        
        user = request.user
        
        if not user.check_password(old_password):
            messages.warning(request, "Old Password doesn't match. Please Try Again!")
            return redirect('password_change')
        
        if len(new_password1)< 8:
            messages.warning(request, "Password must be at least 8 characters long")
            return redirect('password_change')
        
        if old_password == new_password1:
            messages.warning(request, "New Password can't be same as Old Password")
            return redirect('password_change')
        
        if new_password1 != new_password2:
            messages.warning(request, "New Passwords doesn't match. Please Try Again!")
            return redirect('password_change')
        
        user.set_password(new_password1)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, "password change successful. your new password would take effect on next login.")
        return redirect('password_change_done')


# Error Pages
def custom_bad_request_view(request, exception=None):
    return render(request, '400.html', status=400)

def custom_page_not_found_view(request, exception=None):
    return render(request, 'Dashboard/404.html', status=404)

def custom_error_view(request, exception=None):
    return render(request, '500.html', status=500)