from django.db import models

from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin 

# Create your models here.

class EmployeeModelManager(BaseUserManager):
    
    def create_user(self,name,surname,phone_number,position,password,department,**extra_fields,):
        if not surname:
            raise ValueError(_('Surname field must be filled'))
        user = self.model()
        user.name = name
        user.surname = surname
        user.phone_number = phone_number
        user.position = position
        user.department = department
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,name,surname,phone_number,password,position,department,**extra_fields,):

        user = self.model()
        user.name = name
        user.surname = surname
        user.phone_number = phone_number
        user.position = position
        user.department = department
        user.set_password(password)
        user.save()

        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)   

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff = True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser = True'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active = True'))

        return user 

        # MAKE IT WORK!

class Employee(AbstractBaseUser,PermissionsMixin):
    username = None
    email = None
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30,unique=True)
    phone_number = models.IntegerField(null=True)
    position = models.CharField(max_length=70,null=True)

    USERNAME_FIELD = 'surname'
    REQUIRED_FIELDS = ['name','phone_number','position']

    objects = EmployeeModelManager()

    def is_staff(self):
        return self.is_staff

    
    def is_superuser(self):        
        return self.is_superuser


    def is_active(self):
        return self.is_active

    def __str__(self):
        return f"{self.surname} {self.name} {self.phone_number} {self.position}"