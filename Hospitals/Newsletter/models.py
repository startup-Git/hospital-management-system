from django.db import models

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
)

class Subscriber(models.Model):
    mail = models.CharField(max_length=100,)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return self.mail