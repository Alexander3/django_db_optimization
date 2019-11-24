from django.contrib import admin
from main.models import Customer


@admin.register(Customer)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "manager")
    search_fields = ("first_name", "last_name", "phone_number")
    ordering = ("first_name",)
