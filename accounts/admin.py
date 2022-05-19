from django.contrib import admin
from .models import User, Customer, Agent


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'is_customer', 'is_agent')
    ordering = ('first_name',)
    search_fields = ('first_name', )
    list_filter = ('first_name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    ordering = ('user',)
    search_fields = ('user', 'phone_number')
    list_filter = ('user', 'created_at',)


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'company')
    ordering = ('user',)
    search_fields = ('user', 'phone_number')
    list_filter = ('user', 'created_at',)
