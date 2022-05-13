from django.contrib import admin

from .models import Employee,Department

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('surname','name','phone_number','position',)

class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ['name']

admin.site.register(Employee,EmployeeAdmin)    
admin.site.register(Department,DepartmentAdmin)