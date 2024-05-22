from django.contrib import admin
from Newsletter.models import Subscriber
# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('mail', 'status', 'created_on', 'id')
    list_filter = ('status',)
    search_fields = ['mail', 'created_on', 'id']

admin.site.register(Subscriber, SubscriberAdmin)

