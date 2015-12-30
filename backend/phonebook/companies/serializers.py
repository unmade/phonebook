from rest_framework import serializers

from contacts.serializers import PhoneSerializer, EmailSerializer
from .models import Company, Center, Division


class CompanySerializer(serializers.ModelSerializer):
    ceo = serializers.StringRelatedField()
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Company


class CompanyURLSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField(source='get_absolute_api_url')

    class Meta:
        model = Company
        fields = ('name', 'url')


class CenterSerializer(serializers.ModelSerializer):
    head = serializers.StringRelatedField()
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Center


class CenterURLSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField(source='get_absolute_api_url')

    class Meta:
        model = Center
        fields = ('number', 'name', 'url')


class DivisionSerializer(serializers.ModelSerializer):
    head = serializers.StringRelatedField()
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Division


class DivisionURLSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField(source='get_absolute_api_url')

    class Meta:
        model = Division
        fields = ('number', 'name', 'url')
