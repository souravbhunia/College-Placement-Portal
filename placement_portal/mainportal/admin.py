from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class UserStudent(admin.ModelAdmin):
    list_display=('name','id','email','HS_marks','current_cgpa','current_backlogs')