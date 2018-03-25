from django.core.management import BaseCommand
from elasticsearch_dsl import Index

from search.doctypes import EmployeeIndex


class Command(BaseCommand):

    def handle(self, **options):
        index = Index(EmployeeIndex._doc_type.index)
        index.delete(ignore=404)

        EmployeeIndex.init()
        for employee in EmployeeIndex.get_index_queryset():
            EmployeeIndex.from_model(employee).save()
