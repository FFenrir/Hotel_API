from django.contrib import admin

from .models import Client

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['surname','name','phone_number','email']

admin.site.register(Client,ClientAdmin)   