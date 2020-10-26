import pytest
from rest_framework.test import APIClient
from django.urls import reverse_lazy

from .models import Reservation


@pytest.fixture
def client():
    client = APIClient()
    return client


def test_get_view(client):
    """
    Test if index view is working a all.
    """
    response = client.get("", {})
    assert response.status_code == 200


@pytest.mark.django_db
def test_auth_to_fail(client):
    """
    Admin login. Testing authentication.
    """
    client.login(username='test_1', password='passwords_are_for_noobs')
    response = client.get(reverse_lazy('request'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_auth_to_pass(client):
    """
    Admin login. Testing authentication.
    """
    client.login(username='test_1', password='test_1')
    response = client.get(reverse_lazy('request'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_reservation_list(client):
    response = client.get(reverse_lazy('reservation_api'), {}, format='json')

    assert response.status_code == 200
    assert Reservation.objects.count() == len(response.data)
