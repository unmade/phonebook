import factory
from pytest_factoryboy import register
from faker import Factory as FakerFactory

from employees.models import Employee, FirstName, Patronymic, Surname

faker = FakerFactory.create()


@register
class FirstNameFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttributeSequence(lambda s, x: f'{faker.first_name()}{x}')

    class Meta:
        model = FirstName


@register
class PatronymicFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttributeSequence(lambda s, x: f'{faker.name()}{x}')

    class Meta:
        model = Patronymic


@register
class SurnameFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttributeSequence(lambda s, x: f'{faker.last_name()}{x}')

    class Meta:
        model = Surname


@register
class EmployeeFactory(factory.django.DjangoModelFactory):
    surname = factory.SubFactory(SurnameFactory)
    firstname = factory.SubFactory(FirstNameFactory)
    patronymic = factory.SubFactory(PatronymicFactory)

    class Meta:
        model = Employee
