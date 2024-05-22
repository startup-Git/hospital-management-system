from django.urls import path
from . import views

urlpatterns = [
    path('', views.condition, name='condition'),
]
