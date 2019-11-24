import pytest
from django.conf import settings
from django.urls import reverse

from django_db_optimization.settings import DATABASES
from main.models import Customer
from tests.utils import timeit


@pytest.fixture(autouse=True, scope="session")
def django_db_setup():
    """Use real database"""
    settings.DATABASES["default"] = DATABASES


def test_admin(django_assert_num_queries, admin_client):
    with django_assert_num_queries(5):
        response = admin_client.get(
            f"{reverse('admin:main_customer_changelist')}?q=decker"
        )

        assert response.status_code == 200


def test_admin_performance(admin_client):
    url = f"{reverse('admin:main_customer_changelist')}?q=decker"

    result = timeit(
        "admin_client.get(url)", globals={"admin_client": admin_client, "url": url}
    )
    print("\n")
    print(f"Search time: {result}s for {Customer.objects.count()} rows")
