from django.contrib import admin
from About.models import MissionVission, AboutDescription, AboutDescriptionAside

# Register your models here.
class MissionVissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']

admin.site.register(MissionVission, MissionVissionAdmin)

class AboutDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']

admin.site.register(AboutDescription, AboutDescriptionAdmin)

class AboutDescriptionAsideAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'image', 'address', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['image_title', 'phone', 'address']

admin.site.register(AboutDescriptionAside, AboutDescriptionAsideAdmin)
