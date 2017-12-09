# pylint: disable=unused-argument,no-self-use

import factory
from faker import Factory as FakerFactory
from pytest_factoryboy import register

from feedback.models import Feedback

faker = FakerFactory.create()


@register
class FeedbackFactory(factory.django.DjangoModelFactory):
    sender = factory.LazyAttribute(lambda x: faker.name())
    text = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = Feedback
