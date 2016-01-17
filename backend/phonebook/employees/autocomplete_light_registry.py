from django.db.models import Q

from autocomplete_light import shortcuts as autocomplete_light

from companies.models import Company, Center, Division
from .models import Surname, FirstName, Patronymic, Position


autocomplete_light.register(Surname,
    search_fields=('name', ),
    attrs={
        'placeholder': 'Фамилия',
        'data-autocomplete-minimum-characters': 1
    }
)


autocomplete_light.register(FirstName,
    search_fields=('name', ),
    attrs={
        'placeholder': 'Имя',
        'data-autocomplete-minimum-characters': 1
    }
)


autocomplete_light.register(Patronymic,
    search_fields=('name', ),
    attrs={
        'placeholder': 'Отчество',
        'data-autocomplete-minimum-characters': 1
    }
)


autocomplete_light.register(Position,
    search_fields=('name', ),
    attrs={
        'placeholder': 'Должность',
        'data-autocomplete-minimum-characters': 1
    }
)


autocomplete_light.register(Company,
    search_fields=('name', 'short_name', 'full_name'),
    attrs={
        'placeholder': 'Предприятие',
        'data-autocomplete-minimum-characters': 0
    }
)


class CenterAutocompleteRegion(autocomplete_light.AutocompleteModelBase):
    attrs = {
        'placeholder': 'Центр',
        'data-autocomplete-minimum-characters': 0
    }

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        company_id = self.request.GET.get('company_id', None)

        choices = self.choices.all()
        if q:
            choices = choices.filter(Q(name__icontains=q) | Q(number__icontains=q))
        if company_id:
            choices = choices.filter(company_id=company_id)

        return self.order_choices(choices)[0:self.limit_choices]


class DivisionAutocompleteRegion(autocomplete_light.AutocompleteModelBase):
    attrs = {
        'placeholder': 'Отделение/Отдел',
        'data-autocomplete-minimum-characters': 0
    }

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        center_id = self.request.GET.get('center_id', None)

        choices = self.choices.all()
        if q:
            choices = choices.filter(Q(name__icontains=q) | Q(number__icontains=q))
        if center_id:
            choices = choices.filter(center_id=center_id)

        return self.order_choices(choices)[0:self.limit_choices]


autocomplete_light.register(Center, CenterAutocompleteRegion)
autocomplete_light.register(Division, DivisionAutocompleteRegion)
