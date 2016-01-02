from django.contrib import admin

from .models import Category, Phone, Email

# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    search_fields = ('number', )


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    search_fields = ('email', )


admin.site.register(Category)
