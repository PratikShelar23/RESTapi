from django.shortcuts import render
from rest_framework import viewsets 
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class= CompanySerial

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
         try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serial = EmployeeSerial(emps, many=True, context={'request':request})
            return Response(emps_serial.data)
         except Exception as e:
             return Response({
                 'message' : 'Company might not exist !! Error'
             })

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerial

