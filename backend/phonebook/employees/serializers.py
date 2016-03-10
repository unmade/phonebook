from rest_framework import serializers

from contacts.serializers import PhoneSerializer, EmailSerializer
from companies.serializers import CompanyShortSerializer, CenterShortSerializer,\
                                  DivisionShortSerializer, EmployeeShortSerializer
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
                  'company', 'center', 'division',  'place', 'is_retired',
                  'secretary', 'phones', 'emails', 'birthday', 'comment')
