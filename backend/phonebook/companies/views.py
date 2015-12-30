from rest_framework import generics

from .models import Company, Center, Division
from .serializers import CompanySerializer, CenterSerializer, DivisionSerializer


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.select_related('ceo', 'ceo__firstname', 'ceo__surname')\
                              .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')
    serializer_class = CompanySerializer
    search_fields = ('name', 'short_name')
    filter_fields = ('phones__number', 'emails__email')


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.select_related('ceo', 'ceo__firstname', 'ceo__surname')\
                              .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')
    serializer_class = CompanySerializer


class CenterListAPIView(generics.ListAPIView):
    queryset = Center.objects.select_related('head', 'head__firstname', 'head__surname')\
                             .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')
    serializer_class = CenterSerializer
    search_fields = ('number', 'name')
    filter_fields = ('company', 'phones__number', 'emails__email')


class CenterRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Center.objects.select_related('head', 'head__firstname', 'head__surname')\
                             .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')
    serializer_class = CenterSerializer


class DivisionListAPIView(generics.ListAPIView):
    queryset = Division.objects.select_related('head', 'head__firstname', 'head__surname')\
                               .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')
    serializer_class = DivisionSerializer
    search_fields = ('number', 'name')
    filter_fields = ('center', 'phones__number', 'emails__email')


class DivisionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Division.objects.select_related('head', 'head__firstname', 'head__surname')\
                               .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')
    serializer_class = DivisionSerializer
