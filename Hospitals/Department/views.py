import django
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Department.models import DepartmentDetail

# Create your views here.
def department(request):
    template = loader.get_template('department.html')
    profile = DepartmentDetail.objects.filter(status=1).order_by('-created_on')
    data = {
        'profile':profile,
    }
    return HttpResponse(template.render(data, request))

def departmentDetails(request, slug):
    template = loader.get_template('department-details.html')
    details = DepartmentDetail.objects.get(slug = slug)
    data ={
        'details': details,
    }
    return HttpResponse(template.render(data, request))
