import factory
from faker import Factory as FakerFactory

from contacts.models import Category, Email, Phone

faker = FakerFactory.create()


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttributeSequence(lambda s, x: f'{faker.sentence(nb_words=3)}{x}')

    class Meta:
        model = Category


class EmailFactory(factory.django.DjangoModelFactory):
    email = factory.LazyAttributeSequence(lambda s, x: f'{faker.email()}{x}')
    category = factory.SubFactory(CategoryFactory)
    comment = factory.LazyAttribute(lambda x: faker.sentence(nb_words=10))

    class Meta:
        model = Email


class PhoneFactory(factory.django.DjangoModelFactory):
    number = factory.LazyAttributeSequence(lambda s, x: f'{faker.phone_number()}')
    category = factory.SubFactory(CategoryFactory)
    comment = factory.LazyAttribute(lambda x: faker.sentence(nb_words=10))

    class Meta:
        model = Phone
