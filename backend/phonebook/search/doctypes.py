from django.utils.encoding import force_text
from elasticsearch_dsl import DocType, Text, Completion

from employees.models import Employee


class EmployeeIndex(DocType):
    full_name = Text()
    position = Text()
    company_logo = Text()

    suggest = Completion()

    class Meta:
        index = 'employee'

    @classmethod
    def from_model(cls, instance: Employee):
        return cls(
            meta={
                'id': instance.pk,
            },
            full_name=force_text(instance),
            position=instance.position.name if instance.position else None,
            company_logo=instance.company.logo.url if instance.company else None,
            suggest=force_text(instance).split(),
        )

    @staticmethod
    def get_index_queryset():
        return Employee.objects.select_name().select_job().iterator()
