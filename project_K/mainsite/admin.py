from django.contrib import admin
from .models import *

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id","proj_name", "proj_create")

admin.site.register(Project, ProjectAdmin)

class TasksAdmin(admin.ModelAdmin):
    list_display = ("id","task_name", "status", "priority")

admin.site.register(Tasks,TasksAdmin)

class UsersAdmin(admin.ModelAdmin):
    list_display = ("id","username", "email", "date_joined")

admin.site.register(Users,UsersAdmin)

# TEvCKYp9thef.97