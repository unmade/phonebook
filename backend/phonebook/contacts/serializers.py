from rest_framework import serializers

from .models import Phone, Email


class PhoneSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Phone
        fields = serializers.ALL_FIELDS


class EmailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Email
        fields = serializers.ALL_FIELDS
