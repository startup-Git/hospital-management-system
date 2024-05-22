from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment, name='appointment')
]