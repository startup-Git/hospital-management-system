from django.contrib import admin
from Gallery.models import GalleryImage

# Register your models here.
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'image', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['image_title', 'id']

admin.site.register(GalleryImage, GalleryImageAdmin)
