from django.urls import path
from . import views

urlpatterns = [
    path('', views.department, name='department'),
    path('<slug:slug>/', views.departmentDetails, name='departmentDetails'),
]