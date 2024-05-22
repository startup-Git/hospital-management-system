"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import statistics
from xml.etree.ElementInclude import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('Home.urls')),
    path('Department/', include('Department.urls')),
    path('Blog/', include('Blog.urls')),
    path('About-us/', include('About.urls')),
    path('Doctor/', include('Doctor.urls')),
    path('Appointment/', include('Appointment.urls')),
    path('Gallery/', include('Gallery.urls')),
    path('Newsletter/', include('Gallery.urls')),
    path('Privacy-policy/', include('Privacy.urls')),
    path('Terms-condition/', include('Condition.urls')),
    path('accounts/', include('authentication.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


