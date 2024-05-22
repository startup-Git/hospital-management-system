from django.contrib import admin
from Appointment.models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'appointment_date', 'mail', 'phone', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['department', 'doctor', 'appointment_date', 'id']

admin.site.register(Appointment, AppointmentAdmin)
