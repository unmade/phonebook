from django.contrib import admin

from autocomplete_light import shortcuts as autocomplete_light

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
            'classes': ('admin-short-label', ),
            'fields': ('address', ('phones', 'emails'))
        })
    )
    filter_vertical = ('phones', 'emails')
    form = autocomplete_light.modelform_factory(Company, exclude=[])
    list_display = ('name', 'ceo')
    search_fields = ('name', 'full_name', 'short_name')


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {
            'fields': ('number', 'name', 'head', 'company', 'comment')
        }),
        ('Контакты', {
            'classes': ('admin-short-label', ),
            'fields': (('phones', 'emails'), )
        })
    )
    filter_vertical = ('phones', 'emails')
    form = autocomplete_light.modelform_factory(Center, exclude=[])
    list_display = ('number', 'name', 'company', 'head')
    list_display_links = ('number', 'name')
    list_filter = ('company__name', )
    list_select_related = ('company', )
    search_fields = ('number', 'name')


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {
            'fields': ('number', 'name', 'head', 'center', 'comment')
        }),
        ('Контакты', {
            'classes': ('admin-short-label', ),
            'fields': (('phones', 'emails'), )
        })
    )
    filter_vertical = ('phones', 'emails')
    form = autocomplete_light.modelform_factory(Division, exclude=[])
    list_display = ('number', 'name', 'center', 'head')
    list_display_links = ('number', 'name')
    list_filter = ('center', )
    list_select_related = ('center', )
    search_fields = ('number', 'name')


admin.site.register(CompanyCategory)
