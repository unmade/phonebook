from rest_framework import generics

from .models import Company, Center, Division
from .serializers import CompanySerializer, CenterSerializer, DivisionSerializer


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.related_objects.all()
    serializer_class = CompanySerializer
    search_fields = ('name', 'short_name')
    filter_fields = ('phones__number', 'emails__email')


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Company.related_objects.all()
    serializer_class = CompanySerializer


class CenterListAPIView(generics.ListAPIView):
    queryset = Center.related_objects.all()
    serializer_class = CenterSerializer
    search_fields = ('number', 'name')
    filter_fields = ('company', 'phones__number', 'emails__email')


class CenterRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Center.related_objects.all()
    serializer_class = CenterSerializer


class DivisionListAPIView(generics.ListAPIView):
    queryset = Division.related_objects.all()
    serializer_class = DivisionSerializer
    search_fields = ('number', 'name')
    filter_fields = ('center', 'phones__number', 'emails__email')


class DivisionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Division.related_objects.all()
    serializer_class = DivisionSerializer
