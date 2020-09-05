from django.contrib import admin
from .models import *
# Register your models here.

class JobAdmin (admin.ModelAdmin):
    list_display=('company','job_title')

class ProjectsAdmin (admin.ModelAdmin):
    list_display=('title','date')

class VolunteerAdmin (admin.ModelAdmin):
    list_display= ('organization','position','start_date')

class CertificateAdmin (admin.ModelAdmin):
    list_display = ('organization','name')

admin.site.register(Job)
admin.site.register(Project)
admin.site.register(Volunteer)
admin.site.register(Certificates)
