from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Appointment.models import Appointment
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def appointment(request):
    if request.method == "POST":
        name = request.POST.get('User_name')
        phone = request.POST.get('phone_number')
        mail = request.POST.get('Email')
        date = request.POST.get('appointment_date')
        department = request.POST.get('chosse_department')
        doctor = request.POST.get('choose_doctor')
        messages = request.POST.get('message')
        store = Appointment(name = name,mail = mail,phone = phone,appointment_date = date,department = department,doctor = doctor,message = messages)
        store.save() 
    return render(request, 'appointment.html')
