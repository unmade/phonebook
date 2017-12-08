from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Employee, FirstName, Patronymic, Position, Surname


@admin.register(FirstName)
class FirstNameAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Patronymic)
class PatronymicAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Surname)
class SurnameAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('surname', 'firstname', 'patronymic', 'birthday', 'comment')
        }),
        (_('Job'), {
            'fields': ('company', 'center', 'division', 'position', 'place', 'boss', 'is_retired')
        }),
        (_('Contacts'), {
            'fields': (('phones', 'emails'), )
        })
    )
    filter_horizontal = ('phones', 'emails')
    list_display = ('surname', 'firstname', 'company', 'center', 'division')
    list_filter = ('is_retired', 'company', 'center', 'division')
    list_select_related = ('surname', 'firstname', 'company', 'center', 'division')
    autocomplete_fields = ['surname', 'firstname', 'patronymic', 'company', 'center', 'division', 'boss', 'position']
    search_fields = ('surname__name', 'firstname__name')
    ordering = ('surname', 'firstname')
