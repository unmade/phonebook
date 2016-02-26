from django.contrib import admin

from autocomplete_light import shortcuts as autocomplete_light

from .models import FirstName, Patronymic, Surname, Position, Employee

# Register your models here.
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
        ('Данные', {
            'fields': ('surname', 'firstname', 'patronymic', 'birthday', 'comment')
        }),
        ('Место работы', {
            'fields': ('company', 'center', 'division', 'position', 'place', 'boss', 'is_retired')
        }),
        ('Контакты', {
            'classes': ('admin-short-label', ),
            'fields': (('phones', 'emails'), )
        })
    )
    filter_vertical = ('phones', 'emails')
    form = autocomplete_light.modelform_factory(Employee, exclude=[])
    list_display = ('surname', 'firstname', 'company', 'center', 'division')
    list_filter = ('is_retired', 'company', 'center', 'division')
    list_select_related = ('surname', 'firstname', 'company', 'center', 'division')
    search_fields = ('surname__name', 'firstname__name')
    ordering = ('surname', 'firstname')
