import pytest
from django.utils.encoding import force_text


class TestEmployee:

    @pytest.mark.parametrize('given,expected', [
        (
            {'firstname__name': 'Name', 'surname__name': 'Surname', 'patronymic': None},
            'Surname Name',
        ),
        (
            {'firstname': None, 'surname__name': 'Surname', 'patronymic': None},
            'Surname',
        ),
        (
            {'firstname__name': 'Name', 'surname__name': 'Surname', 'patronymic__name': 'Patronymic'},
            'Surname Name Patronymic',
        ),
    ])
    @pytest.mark.django_db
    def test_string_representation(self, employee_factory, given, expected):
        employee = employee_factory(boss=None, **given)
        assert force_text(employee) == expected
