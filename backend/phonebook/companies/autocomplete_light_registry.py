from autocomplete_light import shortcuts as autocomplete_light

from employees.models import Employee


autocomplete_light.register(Employee,
    search_fields=['surname__name', 'firstname__name', 'patronymic__name'],
    attrs={
        'placeholder': 'Руководитель',
        'data-autocomplete-minimum-characters': 1,
    },
)
