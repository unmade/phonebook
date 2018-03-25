from rest_framework import serializers


class SuggestSerializer(serializers.Serializer):
    full_name = serializers.CharField(source='_source.full_name')
    position = serializers.CharField(source='_source.position')
    company_logo = serializers.CharField(source='_source.company_logo')
