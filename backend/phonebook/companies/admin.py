from django.contrib import admin

from .models import CompanyCategory, Company, Center, Division


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'ceo', 'category')
        }),
        ('Дополнительная информация', {
            'fields': ('full_name', 'short_name', 'logo', 'comment',)
        }),
        ('Контакты', {
            'fields': ('address', ('phones', 'emails'))
        })
    )
    filter_vertical = ('phones', 'emails')
    list_display = ('name', 'ceo')
    search_fields = ('name', 'full_name', 'short_name')
    autocomplete_fields = ['ceo']


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {
            'fields': ('number', 'name', 'head', 'company', 'comment')
        }),
        ('Контакты', {
            'fields': (('phones', 'emails'), )
        })
    )
    filter_vertical = ('phones', 'emails')
    list_display = ('number', 'name', 'company', 'head')
    list_display_links = ('number', 'name')
    list_filter = ('company__name', )
    list_select_related = ('company', )
    search_fields = ('number', 'name')
    autocomplete_fields = ['head']


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {
            'fields': ('number', 'name', 'head', 'center', 'comment')
        }),
        ('Контакты', {
            'fields': (('phones', 'emails'), )
        })
    )
    filter_vertical = ('phones', 'emails')
    list_display = ('number', 'name', 'center', 'head')
    list_display_links = ('number', 'name')
    list_filter = ('center', )
    list_select_related = ('center', )
    search_fields = ('number', 'name')
    autocomplete_fields = ['head']


admin.site.register(CompanyCategory)
