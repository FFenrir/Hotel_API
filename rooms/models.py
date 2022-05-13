from django.db import models

# Create your models here.



class Room(models.Model):
    room_number = models.IntegerField()
    status = models.CharField(max_length=100)
    lux  = models.BooleanField()
    booking_started = models.DateField(null=True,blank=True)
    booking_ends = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.room_number)   