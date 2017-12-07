from rest_framework import serializers

from companies.serializers import (
    CenterShortSerializer, CompanyShortSerializer, DivisionShortSerializer, EmployeeShortSerializer
)
from contacts.serializers import EmailSerializer, PhoneSerializer

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    firstname = serializers.StringRelatedField()
    patronymic = serializers.StringRelatedField()
    surname = serializers.StringRelatedField()
    position = serializers.StringRelatedField()
    company = CompanyShortSerializer()
    center = CenterShortSerializer()
    division = DivisionShortSerializer()
    secretary = EmployeeShortSerializer(many=True)
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('id', 'firstname', 'patronymic', 'surname', 'position',
                  'company', 'center', 'division', 'place', 'is_retired',
                  'secretary', 'phones', 'emails', 'birthday', 'comment')
