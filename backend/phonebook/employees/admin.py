from django.contrib import admin

from .models import Employee, FirstName, Patronymic, Position, Surname


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
    list_display = ('surname', 'firstname', 'company', 'center', 'division')
    list_filter = ('is_retired', 'company', 'center', 'division')
    list_select_related = ('surname', 'firstname', 'company', 'center', 'division')
    autocomplete_fields = ['surname', 'firstname', 'patronymic', 'company', 'center', 'division', 'boss', 'position']
    search_fields = ('surname__name', 'firstname__name')
    ordering = ('surname', 'firstname')
