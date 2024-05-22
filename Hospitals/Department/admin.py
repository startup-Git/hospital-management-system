from django.contrib import admin
from Department.models import DepartmentDetail
# Register your models here.
class DepartmentDetailAdmin(admin.ModelAdmin):
    list_display = ('department_name' ,'department_image', 'slug', 'status','created_on', 'id')
    list_filter = ("status",)
    search_fields = ['department_name', 'First_content', 'id']
    prepopulated_fields = {'slug': ('department_name',)}

admin.site.register(DepartmentDetail, DepartmentDetailAdmin)