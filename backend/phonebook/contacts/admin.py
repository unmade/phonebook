from django.contrib import admin

from .models import Category, Phone, Email

# Register your models here.
admin.site.register(Category)
admin.site.register(Phone)
admin.site.register(Email)
