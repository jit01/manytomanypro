from django.contrib import admin
from .models import student, course

class adminstudent(admin.ModelAdmin):
    list_display = ['sid','sname', 'sloc', 'sage']

class admincourse(admin.ModelAdmin):
    list_display = ['cname', 'fee']

admin.site.register(student,adminstudent)
admin.site.register(course,admincourse)
