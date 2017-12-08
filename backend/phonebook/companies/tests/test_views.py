# pylint: disable=unused-argument,no-self-use

import pytest
from django.urls import reverse


class TestCompanyListAPIView:
    url = reverse('companies:api:company-list')

    @pytest.mark.django_db
    def test_response_status_code(self, client, company_factory):
        company_factory.create_batch(5)
        response = client.get(self.url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_num_queries(self, client, django_assert_num_queries, company_factory):
        company_factory.create_batch(5)

        with django_assert_num_queries(6):
            client.get(self.url)


class TestCompanyRetrieveAPIView:

    @pytest.fixture
    def company(self, company_factory):
        return company_factory.create()

    @pytest.mark.django_db
    def test_response_status_code(self, client, company):
        url = company.get_absolute_api_url()
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_num_queries(self, client, django_assert_num_queries, company):
        url = company.get_absolute_api_url()
        with django_assert_num_queries(5):
            client.get(url)


class TestCenterListAPIView:
    url = reverse('companies:api:center-list')

    @pytest.mark.django_db
    def test_response_status_code(self, client, center_factory):
        center_factory.create_batch(5)
        response = client.get(self.url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_num_queries(self, client, django_assert_num_queries, center_factory):
        center_factory.create_batch(5)

        with django_assert_num_queries(6):
            client.get(self.url)


class TestCenterRetrieveAPIView:

    @pytest.fixture
    def center(self, center_factory):
        return center_factory.create()

    @pytest.mark.django_db
    def test_response_status_code(self, client, center):
        url = center.get_absolute_api_url()
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_num_queries(self, client, django_assert_num_queries, center):
        url = center.get_absolute_api_url()
        with django_assert_num_queries(5):
            client.get(url)


class TestDivisionListAPIView:
    url = reverse('companies:api:division-list')

    @pytest.mark.django_db
    def test_response_status_code(self, client, division_factory):
        division_factory.create_batch(5)
        response = client.get(self.url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_num_queries(self, client, django_assert_num_queries, division_factory):
        division_factory.create_batch(5)

        with django_assert_num_queries(6):
            client.get(self.url)


class TestDivisionRetrieveAPIView:

    @pytest.fixture
    def division(self, division_factory):
        return division_factory.create()

    @pytest.mark.django_db
    def test_response_status_code(self, client, division):
        url = division.get_absolute_api_url()
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_num_queries(self, client, django_assert_num_queries, division):
        url = division.get_absolute_api_url()
        with django_assert_num_queries(5):
            client.get(url)
