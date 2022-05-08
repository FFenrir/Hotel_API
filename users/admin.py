from django.contrib import admin

from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('surname','name','phone_number','position',)

admin.site.register(Employee,EmployeeAdmin)    