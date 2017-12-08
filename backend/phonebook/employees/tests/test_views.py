import json

from django.test import TestCase
from django.urls import reverse

from employees.models import Employee, FirstName, Patronymic, Surname
from employees.serializers import EmployeeSerializer


class EmployeeTests(TestCase):
    def setUp(self):
        firstname1, _ = FirstName.objects.get_or_create(name="Василий")
        firstname2, _ = FirstName.objects.get_or_create(name="Валентин")
        patronymic, _ = Patronymic.objects.get_or_create(name="Валентинович")
        surname, _ = Surname.objects.get_or_create(name="Асмус")

        self.employee, _ = Employee.objects.get_or_create(
            firstname=firstname1,
            patronymic=patronymic,
            surname=surname
        )
        Employee.objects.get_or_create(
            firstname=firstname2,
            patronymic=patronymic,
            surname=surname
        )

    def test_list(self):
        url = reverse('employees:api:employee-list')
        response = self.client.get(url)
        self.assertContains(response, "Василий")
        self.assertContains(response, "Валентин")
        self.assertEqual(response.data["count"], 2)

    def test_detail(self):
        url = reverse('employees:api:employee-detail', kwargs={'pk': self.employee.pk})
        response = self.client.get(url)
        data = json.loads(response.content.decode())
        self.assertEqual(data, EmployeeSerializer(self.employee).data)
