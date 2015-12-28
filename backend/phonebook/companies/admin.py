from django.contrib import admin

from .models import CompanyCategory, Company, Center, Division

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    filter_horizontal = ('phones', 'emails')
    search_fields = ('name', 'full_name', 'short_name')


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    filter_horizontal = ('phones', 'emails')
    list_display = ('number', 'name', 'company')
    list_filter = ('company__name', )
    list_select_related = ('company', )
    search_fields = ('number', 'name')


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    filter_horizontal = ('phones', 'emails')
    list_display = ('number', 'name', 'center')
    list_filter = ('center', )
    list_select_related = ('center', )
    search_fields = ('number', 'name')


admin.site.register(CompanyCategory)
