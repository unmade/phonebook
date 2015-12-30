from rest_framework import serializers

from contacts.serializers import PhoneSerializer, EmailSerializer
from companies.serializers import CompanyURLSerializer, CenterURLSerializer, DivisionURLSerializer

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    firstname = serializers.StringRelatedField()
    patronymic = serializers.StringRelatedField()
    surname = serializers.StringRelatedField()
    position = serializers.StringRelatedField()
    company = CompanyURLSerializer()
    center = CenterURLSerializer()
    division = DivisionURLSerializer()
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Employee


class EmployeeURLSerializer(serializers.ModelSerializer):
    firstname = serializers.StringRelatedField()
    patronymic = serializers.StringRelatedField()
    surname = serializers.StringRelatedField()
    url = serializers.ReadOnlyField(source='get_absolute_api_url')

    class Meta:
        model = Employee
        fields = ('firstname', 'patronymic', 'surname', 'url')
