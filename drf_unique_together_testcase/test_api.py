import pytest
from django.urls import reverse
from django.utils.crypto import get_random_string
from rest_framework.test import APIClient

from drf_unique_together_testcase.models import Thing


@pytest.mark.django_db
def test_api(admin_user):
    client = APIClient()
    client.force_login(admin_user)
    thing_list_url = reverse('thing-list')
    name = get_random_string()
    assert client.post(thing_list_url, {'name': name}).status_code == 201
    assert Thing.objects.filter(owner=admin_user).exists()  # Creation worked?
    assert name in client.get(thing_list_url).content.decode()  # Also in response?

    # This fails with error code 400 (validation error) on DRF < 3.8.0,
    # but yields a database integrity error on DRF 3.8.1.
    assert client.post(thing_list_url, {'name': name}).status_code == 400
