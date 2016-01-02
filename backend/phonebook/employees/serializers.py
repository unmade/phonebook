from rest_framework import serializers

from contacts.serializers import PhoneSerializer, EmailSerializer
from companies.serializers import CompanyShortSerializer, CenterShortSerializer, DivisionShortSerializer
from .models import Employee


class EmployeeDetailSerializer(serializers.ModelSerializer):
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


class EmployeeListSerializer(serializers.ModelSerializer):
    firstname = serializers.StringRelatedField()
    patronymic = serializers.StringRelatedField()
    surname = serializers.StringRelatedField()
    position = serializers.StringRelatedField()
    company = serializers.StringRelatedField()
    center = serializers.SlugRelatedField(slug_field='number', read_only=True)
    division = serializers.SlugRelatedField(slug_field='number', read_only=True)
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('id', 'firstname', 'patronymic', 'surname', 'position',
                  'company', 'center', 'division', 'phones', 'emails')
