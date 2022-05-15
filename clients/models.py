from django.db import models

# Create your models here.



class Client(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField()
    preferences = models.TextField()


    def __str__(self):
        return self.surname
