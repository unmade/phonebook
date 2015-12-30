from django.contrib import admin

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
    filter_horizontal = ('phones', 'emails')
    list_display = ('surname', 'firstname', 'company', 'center', 'division')
    list_filter = ('company', 'center', 'division')
    list_select_related = ('surname', 'firstname', 'company', 'center', 'division')
    search_fields = ('surname', 'firstname')
    ordering = ('surname', 'firstname')
