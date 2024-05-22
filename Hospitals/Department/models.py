from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
)

class DepartmentDetail(models.Model):
    department_name = models.CharField(max_length=200, unique=True)
    First_title = models.CharField(max_length=255, blank=True, null=True)
    First_content = HTMLField()
    Hospital_logo = models.ImageField(upload_to='departments')
    
    second_title = models.CharField(max_length=255, blank=True, null=True)
    Second_content = HTMLField()
    department_image = models.ImageField(upload_to='departments')

    third_title = models.CharField(max_length=255, blank=True, null=True)
    third_content = HTMLField()
    author = models.ForeignKey(User, related_name='departmentDetails', on_delete=models.CASCADE)

    Disease_symptoms_1 = models.CharField( max_length=255, blank=True, null=True)
    Disease_symptoms_2 = models.CharField( max_length=255, blank=True, null=True)
    Disease_symptoms_3 = models.CharField( max_length=255, blank=True, null=True)
    Disease_symptoms_4 = models.CharField( max_length=255, blank=True, null=True)
    Disease_symptoms_5 = models.CharField( max_length=255, blank=True, null=True)
    Disease_symptoms_6 = models.CharField( max_length=255, blank=True, null=True)
    Disease_symptoms_7 = models.CharField( max_length=255, blank=True, null=True)
    Disease_symptoms_8 = models.CharField( max_length=255, blank=True, null=True)
    Disease_symptoms_9 = models.CharField( max_length=255, blank=True, null=True)
    Disease_symptoms_10 = models.CharField( max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    fourth_title = models.CharField(max_length=255, blank=True, null=True)
    fourth_content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)

    fiveth_title = models.CharField(max_length=255, blank=True, null=True)
    fiveth_content = HTMLField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return self.department_name
