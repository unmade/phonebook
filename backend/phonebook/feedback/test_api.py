from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from .models import Feedback


class FeedbackTest(TestCase):
    def setUp(self):
        Feedback.objects.get_or_create(sender='John Doe', text='Thank you!')
        Feedback.objects.get_or_create(sender='Adam Smith', text='Please, add something new!', status='DF')
        Feedback.objects.get_or_create(sender='John Doe', text='Nice job, again!')

        self.list_url = reverse('api:feedback-list')

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, 'John Doe')
        self.assertContains(response, 'Adam Smith')
        self.assertContains(response, 'DF')
        self.assertEqual(response.data["count"], 3)

    def test_create(self):
        feedback = {"sender": 'Nuwanda', "text":'Add DPS members, please!'}
        response = self.client.post(self.list_url, feedback, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.count(), 4)
        self.assertEqual(Feedback.objects.get(pk=4).sender, 'Nuwanda')
