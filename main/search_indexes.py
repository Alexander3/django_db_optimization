from haystack import indexes
from main.models import Customer


class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True, use_template=True, template_name="customer_text.txt"
    )
    first_name = indexes.CharField(model_attr="first_name")
    last_name = indexes.CharField(model_attr="last_name")
    phone_number = indexes.CharField(model_attr="phone_number", null=True)

    def get_model(self):
        return Customer
