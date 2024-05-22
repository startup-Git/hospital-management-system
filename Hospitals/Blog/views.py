from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Blog.models import BlogPost

# Create your views here.
def blog(request):
    template = loader.get_template('blog.html')
    BlogList  = BlogPost.objects.filter(status=1).order_by('-created_on')
    data = {
        'BlogList': BlogList,
    }
    return HttpResponse(template.render(data, request))

def blog_post_details(request, slug):
    template = loader.get_template('blog-details.html')
    model = BlogPost.objects.get(slug= slug)
    data = {
       'model': model, 
    }
    return HttpResponse(template.render(data, request))

