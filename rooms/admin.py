from django.contrib import admin

from .models import Room

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ['room_number','status','lux']
    list_filter = ['status','lux']

admin.site.register(Room,RoomAdmin)    