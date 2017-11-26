from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.related_objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ('firstname__name', 'patronymic__name', 'surname__name')
    filter_fields = ('company', 'center', 'division', 'phones__number', 'emails__email')


class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employee.related_objects.all()
    serializer_class = EmployeeSerializer
