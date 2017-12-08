# pylint: disable=unused-argument,no-self-use

import factory
from faker import Factory as FakerFactory
from pytest_factoryboy import register

from companies.models import Center, Company, CompanyCategory, Division
from contacts.tests.conftest import EmailFactory, PhoneFactory
from employees.tests.conftest import EmployeeFactory

faker = FakerFactory.create()


@register
class CompanyCategoryFactory(factory.django.DjangoModelFactory):
    category = factory.LazyAttributeSequence(lambda s, x: faker.word())
    name = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))

    class Meta:
        model = CompanyCategory


@register
class CompanyFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.company)
    ceo = factory.SubFactory(EmployeeFactory)
    category = factory.SubFactory(CompanyCategoryFactory)

    class Meta:
        model = Company

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        for _ in range(3):
            self.phones.add(PhoneFactory())
            self.emails.add(EmailFactory())


@register
class CenterFactory(factory.django.DjangoModelFactory):
    company = factory.SubFactory(CompanyFactory)
    head = factory.SubFactory(EmployeeFactory)
    number = factory.LazyAttribute(lambda x: faker.word()[:10])
    name = factory.LazyAttribute(lambda x: faker.word())
    comment = factory.LazyAttribute(lambda x: faker.paragraph())

    class Meta:
        model = Center

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        for _ in range(3):
            self.phones.add(PhoneFactory())
            self.emails.add(EmailFactory())


@register
class DivisionFactory(factory.django.DjangoModelFactory):
    center = factory.SubFactory(CenterFactory)
    head = factory.SubFactory(EmployeeFactory)
    number = factory.LazyAttribute(lambda x: faker.word()[:10])
    name = factory.LazyAttribute(lambda x: faker.word())
    comment = factory.LazyAttribute(lambda x: faker.paragraph())

    class Meta:
        model = Division

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        for _ in range(3):
            self.phones.add(PhoneFactory())
            self.emails.add(EmailFactory())
