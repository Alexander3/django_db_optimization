from django.contrib import admin
from haystack.admin import SearchChangeList
from main.models import Customer


# Monkey patch, haystack doesn't support newest django :(
def fixed_init(self, *args, **kwargs):
    self.haystack_connection = kwargs.pop("haystack_connection", "default")
    super(SearchChangeList, self).__init__(*args, **kwargs)


SearchChangeList.__init__ = fixed_init


@admin.register(Customer)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "manager_name")
    list_select_related = ("manager",)
    search_fields = ("first_name", "last_name", "phone_number")
    ordering = ("first_name",)

    def manager_name(self, customer: Customer):
        return customer.manager.first_name

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("manager")

    def get_changelist(self, request, **kwargs):
        return SearchChangeList
