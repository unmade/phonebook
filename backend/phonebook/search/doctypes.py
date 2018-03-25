from django.utils.encoding import force_text
from elasticsearch_dsl import DocType, Text

from employees.models import Employee


class EmployeeIndex(DocType):
    full_name = Text()

    class Meta:
        index = 'employee'

    @classmethod
    def from_model(cls, instance: Employee):
        return cls(
            meta={
                'id': instance.pk,
            },
            full_name=force_text(instance),
        )
