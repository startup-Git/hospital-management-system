from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from Newsletter.models import Subscriber

# Create your views here.
def newsletter(request):
    if request.method == "POST":
        Mail = request.POST.get('newsletter')
        Subscriber_list = Subscriber(mail = Mail)
        Subscriber_list.save()
    return redirect('')