from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('sender', 'text', 'created_at', 'status')
    list_editable = ('status', )
    list_filter = ('status',)
