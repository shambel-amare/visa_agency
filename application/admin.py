from django.contrib import admin
from .models import Application


# admin.site.register(Application)
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone_number', 'owner', 'application_type',)
    ordering = ('created_at',)
    search_fields = ('first_name', 'phone_number',)
    list_filter = ('first_name', 'application_type', 'owner')
