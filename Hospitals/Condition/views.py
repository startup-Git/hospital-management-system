from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def condition(request):
    template = loader.get_template('Terms-Conditions.html')
    return HttpResponse(template.render())
