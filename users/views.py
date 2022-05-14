from django.shortcuts import render

from .models import Employee

from .serializers import EmployeeSerializer

from rest_framework import generics

# Create your views here.

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer    