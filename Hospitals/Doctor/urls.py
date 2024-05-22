from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor, name='doctor'),
    path('<slug:slug>/', views.details, name='details')
]