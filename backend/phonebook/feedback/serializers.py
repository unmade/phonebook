from rest_framework import serializers

from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    sender = serializers.CharField()

    class Meta:
        model = Feedback
