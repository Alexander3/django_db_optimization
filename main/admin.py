from django.contrib import admin
from main.models import Customer


@admin.register(Customer)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "manager_name")
    search_fields = ("first_name", "last_name", "phone_number")
    ordering = ("first_name",)

    def manager_name(self, customer: Customer):
        return customer.manager.first_name
