from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
)

class DoctorDetail(models.Model):
    profile = models.ImageField(upload_to='all-doctors')
    name = models.CharField(max_length=255, unique=True)
    specialist = models.CharField(max_length=200, unique=True)
    specialist_description = models.TextField()
    Biography_content = HTMLField()
    # Education
    Graduation_one = models.CharField( max_length=255, blank=True, null=True)
    University_one = models.CharField(max_length=150, blank=True, null=True)
    Graduation_two = models.CharField( max_length=255, blank=True, null=True)
    University_two = models.CharField(max_length=150, blank=True, null=True)
    Graduation_three = models.CharField( max_length=255, blank=True, null=True)
    University_three = models.CharField(max_length=150, blank=True, null=True)
    Graduation_four = models.CharField( max_length=255, blank=True, null=True)
    University_four = models.CharField(max_length=150, blank=True, null=True)
    Graduation_five = models.CharField( max_length=255, blank=True, null=True)
    University_five = models.CharField(max_length=150, blank=True, null=True)
    # Employment
    official_cv = models.FileField(upload_to='documents/')

    Employe_one = models.CharField( max_length=255, blank=True, null=True)
    date_one = models.CharField(max_length=150, blank=True, null=True)
    Employe_two = models.CharField( max_length=255, blank=True, null=True)
    date_two = models.CharField(max_length=150, blank=True, null=True)
    Employe_three = models.CharField( max_length=255, blank=True, null=True)
    date_three = models.CharField(max_length=150, blank=True, null=True)
    Employe_four = models.CharField( max_length=255, blank=True, null=True)
    date_four = models.CharField(max_length=150, blank=True, null=True)
    Employe_five = models.CharField( max_length=255, blank=True, null=True)
    date_five = models.CharField(max_length=150, blank=True, null=True)
    # membership
    slug = models.SlugField(max_length=255, unique=True)

    Membership_one = models.CharField( max_length=255, blank=True, null=True)
    Membership_two = models.CharField( max_length=255, blank=True, null=True)
    Membership_three = models.CharField( max_length=255, blank=True, null=True)
    Membership_four = models.CharField( max_length=255, blank=True, null=True)
    Membership_five = models.CharField( max_length=255, blank=True, null=True)
    Membership_six = models.CharField( max_length=255, blank=True, null=True)
    # doctor visit time
    author = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)

    Saturday = models.CharField(max_length=50, blank=True, null=True)
    Saturday_time = models.CharField(max_length=30, blank=True, null=True)
    Sunday  = models.CharField(max_length=50, blank=True, null=True)
    Sunday_time = models.CharField(max_length=30, blank=True, null=True)
    Monday = models.CharField(max_length=50, blank=True, null=True)
    Monday_time = models.CharField(max_length=30, blank=True, null=True)
    Tuesday = models.CharField(max_length=50, blank=True, null=True)
    Tuesday_time = models.CharField(max_length=30, blank=True, null=True)
    Wednesday = models.CharField(max_length=50, blank=True, null=True)
    Wednesday_time = models.CharField(max_length=30, blank=True, null=True)
    Thursday = models.CharField(max_length=50, blank=True, null=True)
    Thursday_time = models.CharField(max_length=30, blank=True, null=True)
    Friday = models.CharField(max_length=50, blank=True, null=True)
    Friday_time = models.CharField(max_length=30, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return self.name


class PatientsReview(models.Model):
    name = models.CharField(max_length=255)
    Email = models.CharField(max_length=100)
    messages = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return self.name