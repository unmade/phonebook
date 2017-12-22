from rest_framework import generics

from .models import Center, Company, Division
from .serializers import CenterSerializer, CompanySerializer, DivisionSerializer


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all().select_ceo().prefetch_contacts()
    serializer_class = CompanySerializer
    search_fields = ('name', 'short_name')
    filter_fields = ('phones__number', 'emails__email')


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all().select_ceo().prefetch_contacts()
    serializer_class = CompanySerializer


class CenterListAPIView(generics.ListAPIView):
    queryset = Center.objects.all().select_head().prefetch_contacts()
    serializer_class = CenterSerializer
    search_fields = ('number', 'name')
    filter_fields = ('company', 'phones__number', 'emails__email')


class CenterRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Center.objects.all().select_head().prefetch_contacts()
    serializer_class = CenterSerializer


class DivisionListAPIView(generics.ListAPIView):
    queryset = Division.objects.all().select_head().prefetch_contacts()
    serializer_class = DivisionSerializer
    search_fields = ('number', 'name')
    filter_fields = ('center', 'phones__number', 'emails__email')


class DivisionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Division.objects.all().select_head().prefetch_contacts()
    serializer_class = DivisionSerializer
