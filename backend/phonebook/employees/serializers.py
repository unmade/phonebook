from rest_framework import serializers

from contacts.serializers import PhoneSerializer, EmailSerializer
from companies.serializers import CompanyShortSerializer, CenterShortSerializer, DivisionShortSerializer
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    firstname = serializers.StringRelatedField()
    patronymic = serializers.StringRelatedField()
    surname = serializers.StringRelatedField()
    position = serializers.StringRelatedField()
    company = CompanyShortSerializer()
    center = CenterShortSerializer()
    division = DivisionShortSerializer()
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Employee
