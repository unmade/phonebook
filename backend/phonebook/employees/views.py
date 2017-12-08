from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.select_name().select_job().prefetch_contacts().prefetch_secretaries()
    serializer_class = EmployeeSerializer
    search_fields = ('firstname__name', 'patronymic__name', 'surname__name')
    filter_fields = ('company', 'center', 'division', 'phones__number', 'emails__email')


class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.select_name().select_job().prefetch_contacts().prefetch_secretaries()
    serializer_class = EmployeeSerializer
