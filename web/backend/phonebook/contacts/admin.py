from django.contrib import admin

from .models import Category, Email, Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    search_fields = ('number', )


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    search_fields = ('email', )


admin.site.register(Category)
