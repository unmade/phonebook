from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FeedbackSerializer
