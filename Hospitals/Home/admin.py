from django.contrib import admin
from Home.models import ShortDoctorProfile, ShortDoctorTitle, Slider, SliderContent
from Home.models import ShortAbout, ShortDepartment
from Home.models import CounterSection, ChooseU
# Register your models here SliderAdmin
class SliderAdmin(admin.ModelAdmin):
    list_display = ('Image', 'Time', 'id')

admin.site.register(Slider, SliderAdmin)
    
# Register your models here SliderContentAdmin 
class SliderContentAdmin(admin.ModelAdmin):
    list_display = (
            'slider_header', 
            'slider_description', 
            'button_one', 
            'button_two', 
            'time'
    )

admin.site.register(SliderContent, SliderContentAdmin)

# Register your models here ShortAbout
class ShortAboutAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'about_image_one',
            'about_image_two', 
            'image_two_title', 
            'about_image_three', 
            'header_description', 
            'about_header', 
            'header_paragraph', 
            'about_services_icon', 
            'about_services_header', 
            'about_services_paragraph', 
            'time'
    )

admin.site.register(ShortAbout, ShortAboutAdmin)
 
# Register your models here ShortAbout
class ShortDepartmentAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'department_description',
            'department_header', 
            'department_image', 
            'department_image_title', 
            'department_image_paragraph', 
            'department_icon_image', 
            'department_icon_title', 
            'department_icon_paragraph', 
            'department_details_button', 
            'time'
    )

admin.site.register(ShortDepartment, ShortDepartmentAdmin)


# Register your models here CounterSection
class CounterSectionAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'background_video', 
            'counter_icon', 
            'counter_icon_title', 
            'counter_value', 
            'time'
    )

admin.site.register(CounterSection, CounterSectionAdmin)

# Register your models here ChooseU 
class ChooseUAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'choose_us_image', 
            'choose_us_description', 
            'collapsible_header_icon', 
            'collapsible_header',
            'collapsible_paragraph', 
            'time'
    )

admin.site.register(ChooseU, ChooseUAdmin)

# Register your models here ShortDoctorTitleAdmin
class ShortDoctorTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'header_description', 'header_title', 'time')

admin.site.register(ShortDoctorTitle, ShortDoctorTitleAdmin)

# Register your models here ShortDoctorProfileAdmin
class ShortDoctorProfileAdmin(admin.ModelAdmin):
    list_display = (
            'id', 
            'doctor_profile', 
            'doctor_name', 
            'specialist',
            'facebook_icon_class',
            'facebook_profile',
            'linkedin_icon_class',
            'linkedin_profile',
            'whatsapp_icon_class',
            'whatsapp_profile',
            'time')

admin.site.register(ShortDoctorProfile, ShortDoctorProfileAdmin)