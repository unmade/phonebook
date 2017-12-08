from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Center, Company, CompanyCategory, Division


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'ceo', 'category')
        }),
        (_('Additional info'), {
            'fields': ('full_name', 'short_name', 'logo', 'comment', )
        }),
        (_('Contacts'), {
            'fields': ('address', ('phones', 'emails'))
        })
    )
    filter_horizontal = ('phones', 'emails')
    list_display = ('name', 'ceo')
    search_fields = ('name', 'full_name', 'short_name')
    autocomplete_fields = ['ceo']


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('number', 'name', 'head', 'company', 'comment')
        }),
        (_('Contacts'), {
            'fields': (('phones', 'emails'), )
        })
    )
    filter_horizontal = ('phones', 'emails')
    list_display = ('number', 'name', 'company', 'head')
    list_display_links = ('number', 'name')
    list_filter = ('company__name', )
    list_select_related = ('company', )
    search_fields = ('number', 'name')
    autocomplete_fields = ['head']


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('number', 'name', 'head', 'center', 'comment')
        }),
        (_('Contacts'), {
            'fields': (('phones', 'emails'), )
        })
    )
    filter_horizontal = ('phones', 'emails')
    list_display = ('number', 'name', 'center', 'head')
    list_display_links = ('number', 'name')
    list_filter = ('center', )
    list_select_related = ('center', )
    search_fields = ('number', 'name')
    autocomplete_fields = ['head']


admin.site.register(CompanyCategory)
