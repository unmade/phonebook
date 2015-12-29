from rest_framework import serializers

from contacts.serializers import PhoneSerializer, EmailSerializer

from .models import Company, Center, Division


class CompanySerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Company


class CenterSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Center


class DivisionSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Division
