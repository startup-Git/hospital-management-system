from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from Doctor.models import DoctorDetail,PatientsReview

# Create your views here.
def doctor(request):
    template = loader.get_template('findDoctor.html')
    doctor_list  = DoctorDetail.objects.filter(status=1).order_by('-created_on')
    data = {
       'doctor_list': doctor_list, 
    }
    return HttpResponse(template.render(data, request))

def details(request, slug):
    template = loader.get_template('doctor-details.html')
    details = DoctorDetail.objects.get(slug = slug)
    data = {
       'details':details, 
    }
    if request.method == "POST":
        message = request.POST.get('messages')
        user = request.POST.get('user_name')
        user_mail = request.POST.get('user_mail')
        store = PatientsReview(
            name = user,
            Email = user_mail,
            messages = message
        )
        store.save()
    return HttpResponse(template.render(data, request))
