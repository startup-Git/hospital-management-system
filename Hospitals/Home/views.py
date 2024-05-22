from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from Home.models import ChooseU, ShortDoctorProfile, ShortDoctorTitle, Slider, SliderContent
from Home.models import ShortAbout, ShortDepartment, CounterSection
from Blog.models import BlogPost
from Appointment.models import Appointment
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    slide = Slider.objects.all()
    content = SliderContent.objects.all()
    about = ShortAbout.objects.all()
    # department pagination
    department = ShortDepartment.objects.all()
    paginator = Paginator(department,4)
    page_number = request.GET.get('page')
    department_final = paginator.get_page(page_number)
    count_page = department_final.paginator.num_pages
    # department pagination end
    counter = CounterSection.objects.all()
    chooseUS = ChooseU.objects.all()
    doctorHeader = ShortDoctorTitle.objects.all()
    doctorProfile = ShortDoctorProfile.objects.all()
    blogposts = BlogPost.objects.filter(status=1).order_by('-created_on')[:3]
    # Appointment_list = Appointment.objects.all()
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
    data = {
        'slide': slide,
        'content': content,
        'about': about,
        # department & department pagination
        'department': department_final,
        'count_page': [n+1 for n in range(count_page)],
        # department & department pagination end
        'counter': counter,
        'chooseUS': chooseUS,
        'doctorHeader': doctorHeader,
        'doctorProfile': doctorProfile,
        'blogposts': blogposts,
    }
    return HttpResponse(template.render(data, request))