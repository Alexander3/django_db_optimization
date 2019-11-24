import timeit

import pytest

from django.conf import settings
from django.urls import reverse
from django_db_optimization.settings import DATABASES


@pytest.fixture(autouse=True, scope="session")
def django_db_setup():
    settings.DATABASES["default"] = DATABASES


def test_admin(django_assert_num_queries, admin_client):
    with django_assert_num_queries(5):
        response = admin_client.get(f"{reverse('admin:main_customer_changelist')}?q=a")

        assert response.status_code == 200
        assert len(response.context_data["cl"].result_list) == 100


def test_admin_performance(admin_client):
    url = f"{reverse('admin:main_customer_changelist')}?q=a"

    postgres = timeit.timeit(lambda: admin_client.get(url), number=100)
    print("\n")
    print(f"postgres without index {round(postgres, 2)}s")
