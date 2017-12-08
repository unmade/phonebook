# pylint: disable=unused-argument,no-self-use

import pytest
from django.urls import reverse


class TestEmployeeListAPIView:
    url = reverse('employees:api:employee-list')

    @pytest.mark.django_db
    def test_response_status_code(self, client, employee_factory):
        employee_factory.create_batch(5, boss__boss=None)
        response = client.get(self.url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_num_queries(self, client, django_assert_num_queries, employee_factory):
        employee_factory.create_batch(10, boss=None)
        with django_assert_num_queries(5):
            client.get(self.url)


class TestEmployeeRetrieveAPIView:

    @pytest.fixture
    def employee(self, employee_factory):
        return employee_factory.create(boss__boss=None)

    @pytest.mark.django_db
    def test_response_status_code(self, client, employee):
        url = employee.get_absolute_api_url()
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_num_queries(self, client, django_assert_num_queries, employee):
        url = employee.get_absolute_api_url()
        with django_assert_num_queries(4):
            client.get(url)
