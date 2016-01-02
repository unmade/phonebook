from rest_framework import serializers

from contacts.serializers import PhoneSerializer, EmailSerializer
from .models import Company, Center, Division


class CompanySerializer(serializers.ModelSerializer):
    ceo = serializers.StringRelatedField()
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Company


class CenterSerializer(serializers.ModelSerializer):
    head = serializers.StringRelatedField()
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Center


class DivisionSerializer(serializers.ModelSerializer):
    head = serializers.StringRelatedField()
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Division


class CompanyShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'logo')


class CenterShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ('id', 'number', 'name')


class DivisionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ('id', 'number', 'name')
