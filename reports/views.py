from distutils.ccompiler import gen_lib_options
from django.shortcuts import render

from rest_framework import generics

from .models import Report

from .serializers import ReportSerializer

# Create your views here.


class ReportListView(generics.ListAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReprtDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer    