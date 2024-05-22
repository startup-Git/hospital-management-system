from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def privacy(request):
    template = loader.get_template('Privacy-Policy.html')
    return HttpResponse(template.render())
