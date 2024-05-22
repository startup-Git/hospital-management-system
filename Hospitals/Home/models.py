from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Slider(models.Model):
    Image = models.ImageField(upload_to = 'Slider')
    Time = models.DateTimeField(auto_now_add=True)

class SliderContent(models.Model):
    slider_header = models.CharField(max_length = 255)
    slider_description = HTMLField()
    button_one = models.CharField(max_length=50)
    button_two = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

class ShortAbout(models.Model):
    about_image_one = models.ImageField(upload_to = 'Home-page' , blank=True, null=True)
    about_image_two = models.ImageField(upload_to = 'Home-page', blank=True, null=True)
    image_two_title = models.CharField(max_length=100, blank=True, null=True)
    about_image_three = models.ImageField(upload_to = 'Home-page', blank=True, null=True)
    # text section
    header_description = models.CharField(max_length=100, blank=True, null=True)
    about_header = models.CharField(max_length=255, blank=True, null=True)
    header_paragraph = models.TextField(blank=True, null=True)
    # about services
    about_services_icon = models.CharField(max_length=100, blank=True, null=True)
    about_services_header = models.CharField(max_length=200, blank=True, null=True)
    about_services_paragraph = models.TextField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

class ShortDepartment(models.Model):
    # departments heading text
    department_description = models.CharField(max_length=100, blank=True, null=True)
    department_header = models.CharField(max_length=255, blank=True, null=True)
    # departments card
    department_image = models.ImageField(upload_to = 'Home-page' , blank=True, null=True)
    department_image_title = models.CharField(max_length=100, blank=True, null=True)
    department_image_paragraph = models.TextField(blank=True, null=True)
    # departments card hover
    department_icon_image = models.ImageField(upload_to = 'Home-page' , blank=True, null=True)
    department_icon_title = models.CharField(max_length=100, blank=True, null=True)
    department_icon_paragraph = models.TextField(blank=True, null=True)
    department_details_button = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)

class CounterSection(models.Model):
    background_video = models.FileField(upload_to = 'videos', blank=True, null=True)
    counter_icon = models.CharField(max_length=100, blank=True, null=True)
    counter_icon_title = models.CharField(max_length=200, blank=True, null=True)
    counter_value = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)


class ChooseU(models.Model):
    choose_us_image = models.ImageField(upload_to = 'Home-page' , blank=True, null=True)
    choose_us_description = models.CharField(max_length=200, blank=True, null=True)
    collapsible_header_icon = models.CharField(max_length=100, blank=True, null=True)
    collapsible_header = models.CharField(max_length=255, blank=True, null=True)
    collapsible_paragraph = HTMLField()
    time = models.DateTimeField(auto_now_add=True)

    
class ShortDoctorTitle(models.Model):
    header_description = models.CharField(max_length=100, blank=True, null=True)
    header_title = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)


class ShortDoctorProfile(models.Model):
    doctor_profile = models.ImageField(upload_to = 'Home-page' , blank=True, null=True)
    doctor_name = models.CharField(max_length=120, blank=True, null=True)
    specialist = models.CharField(max_length=255, blank=True, null=True)
    facebook_icon_class = models.CharField(max_length=100, blank=True, null=True)
    facebook_profile = models.CharField(max_length=100, blank=True, null=True)
    linkedin_icon_class = models.CharField(max_length=100, blank=True, null=True)
    linkedin_profile = models.CharField(max_length=100, blank=True, null=True)
    whatsapp_icon_class = models.CharField(max_length=100, blank=True, null=True)
    whatsapp_profile = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)


    

    



