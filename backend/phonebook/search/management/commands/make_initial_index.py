from django.core.management import BaseCommand

from employees.models import Employee
from search.doctypes import EmployeeIndex


class Command(BaseCommand):

    def handle(self, **options):
        EmployeeIndex.init()
        for employee in Employee.objects.select_name().iterator():
            EmployeeIndex.from_model(employee).save()
