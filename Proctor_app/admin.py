from django.contrib import admin
from .models import Student,Proctor,Faculty,Parent,HOD,Department  # Import your models here
from django.contrib.admin import AdminSite

# Register your models with the admin site
admin.site.register(Student)
admin.site.register(Proctor)
admin.site.register(Faculty)
admin.site.register(Parent)
admin.site.register(HOD)
admin.site.register(Department)


# Override the site header
admin.site.site_header = 'S J C Institute Of Technology'

class CustomAdminSite(AdminSite):
    login_template = 'admin/admin_login.html'

admin_site = CustomAdminSite(name='customadmin')