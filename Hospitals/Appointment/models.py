from django.db import models

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
)

class Appointment(models.Model):
    name = models.CharField(max_length=150,)
    mail = models.CharField(max_length=150,)
    phone = models.CharField(max_length= 20,)
    appointment_date = models.CharField(max_length=50,)
    department = models.CharField(max_length=150,)
    doctor = models.CharField(max_length=150,)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.mail

