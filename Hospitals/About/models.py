from django.db import models
from tinymce.models import HTMLField

STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
)

# Create your models here.
class MissionVission(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = HTMLField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return self.title


class AboutDescription(models.Model):
    title = models.CharField(max_length=255, unique=True,)
    content = HTMLField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return self.title


class AboutDescriptionAside(models.Model):
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='about-post', blank=True, null=True)
    image_title = models.CharField(max_length=200, blank=True, null=True)
    address = HTMLField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    phone_link = models.CharField(max_length=50, blank=True, null=True)
    button = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return self.image_title