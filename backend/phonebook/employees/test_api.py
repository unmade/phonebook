import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import FirstName, Patronymic, Surname, Employee
from .serializers import EmployeeSerializer


class EmployeeTests(TestCase):
    def setUp(self):
        firstname1 = FirstName.objects.get_or_create(name="Василий")
        firstname2 = FirstName.objects.get_or_create(name="Валентин")
        patronymic = Patronymic.objects.get_or_create(name="Валентинович")
        surname = Surname.objects.get_or_create(name="Асмус")
        employee1 = Employee.objects.get_or_create(
            firstname = firstname1[0],
            patronymic = patronymic[0],
            surname = surname[0]
        )
        employee2 = Employee.objects.get_or_create(
            firstname = firstname2[0],
            patronymic = patronymic[0],
            surname = surname[0]
        )
        self.serialized_employee = EmployeeSerializer(employee1[0])

        self.list_url = reverse('api:employee-list')
        self.detail_url = reverse('api:employee-detail', kwargs={'pk': employee1[0].pk})


    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, "Василий")
        self.assertContains(response, "Валентин")
        self.assertEqual(response.data["count"], 2)

    def test_detail(self):
        response = self.client.get(self.detail_url)
        data = json.loads(response.content.decode())
        self.assertEquals(data, self.serialized_employee.data)
