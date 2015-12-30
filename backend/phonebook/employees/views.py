from django.shortcuts import render

from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.select_related('firstname', 'patronymic', 'surname', 'company', 'center', 'division')\
                               .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')
    serializer_class = EmployeeSerializer
    search_fields = ('firstname__name', 'patronymic__name', 'surname__name')
    filter_fields = ('company', 'center', 'division', 'phones__number', 'emails__email')


class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.select_related('firstname', 'patronymic', 'surname', 'company', 'center', 'division')\
                              .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')
    serializer_class = EmployeeSerializer
