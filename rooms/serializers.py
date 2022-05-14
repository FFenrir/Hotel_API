from rest_framework import serializers

from .models import Room



class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('room_number','status','lux','booking_started','booking_ends',)