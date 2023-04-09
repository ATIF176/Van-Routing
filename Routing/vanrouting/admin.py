from django.contrib import admin
from .models import Vaninfo, Institutes_details

# Register your models here.
class VanAdmin(admin.ModelAdmin):
    list_display = ('van_no', 'driver_name')
    prepopulated_fields = {'van_slug':('van_no', )}

class InstituteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'institute_slug':('institute_name', )}


admin.site.register(Vaninfo, VanAdmin)
admin.site.register(Institutes_details, InstituteAdmin)