from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Gallery.models import GalleryImage

# Create your views here.
def gallery(request):
    template = loader.get_template('gallery.html')
    photo = GalleryImage.objects.filter(status=1).order_by('-created_on')
    data = {
        'photo': photo,
    }
    return HttpResponse(template.render(data, request))
