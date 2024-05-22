from django.db import models


STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
)
# Create your models here.
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='Gallery')
    image_title = models.CharField(max_length=50, unique= True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.image_title

