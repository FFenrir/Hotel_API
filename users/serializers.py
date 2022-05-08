from sqlite3 import adapt
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Employee



class EmployeeRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length = 20)
    surname = serializers.CharField(max_length = 30)
    phone_number = serializers.IntegerField()
    position = serializers.CharField(max_length = 70)
    
    class Meta:
        model = Employee
        fields = ('name','surname','phone_number','position',)

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'surname': self.validated_data.get('surname',''),
            'phone_number':self.validated_data.get('phone_number',''),
            'position':self.validated_data.get('position',''),
            'password1': self._validated_data.get('password1',''),
            'password2': self.validated_data.get('password2',''),          
        }    

    def save(self,request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.name = self.cleaned_data.get('name')
        user.surname = self.cleaned_data.get('surname')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.position = self.cleaned_data.get('position')
        user.save()
        adapter.save_user(request,user,self)
        return user    