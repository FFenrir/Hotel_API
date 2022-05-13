from django.contrib import admin

from .models import Report

# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    model = Report
    list_display = ['room','report_title','report_left_by','report_left_to']

admin.site.register(Report,ReportAdmin)