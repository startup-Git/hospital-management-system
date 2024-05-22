from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
)

class BlogPost(models.Model):
    image = models.ImageField(upload_to='blog-post')
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    blog_department = models.CharField(max_length=80, unique=True)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return self.title

