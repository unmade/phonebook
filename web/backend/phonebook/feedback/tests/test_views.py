import pytest
from django.urls import reverse

from feedback.models import Feedback


class TestFeedbackListAPIView:
    url = reverse('feedback:api:feedback-list')

    @pytest.mark.django_db
    def test_response_status_code(self, client, feedback_factory):
        feedback_factory.create_batch(5)
        response = client.get(self.url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_assert_num_queries(self, client, django_assert_num_queries, feedback_factory):
        feedback_factory.create_batch(5)
        with django_assert_num_queries(2):
            client.get(self.url)

    @pytest.mark.django_db
    def test_create(self, client):
        data = {'sender': 'Junior', 'text': 'Wow! This is great!'}
        response = client.post(self.url, data)
        assert response.status_code == 201

        feedback = Feedback.objects.filter().first()
        assert feedback.sender == data['sender']
        assert feedback.text == data['text']
