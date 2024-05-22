from django.contrib import admin
from Doctor.models import DoctorDetail, PatientsReview

# Register your models here.
class DoctorDetailAdmin(admin.ModelAdmin):
    list_display = ('name' ,'profile', 'slug', 'author', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['name', 'specialist']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(DoctorDetail, DoctorDetailAdmin)

class PatientsReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'Email', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['name', 'Email']

admin.site.register(PatientsReview, PatientsReviewAdmin)
