import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        pass


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def register_test_user(api_client):
    ep = reverse('register-user-list')
    payload = {
        'email': 'test_login@tesmail.com',
        'username': 'login_user',
        'password1': 'userpass1234',
        'password2': 'userpass1234',
        'first_name': 'test',
        'last_name': 'login'
    }

    response = api_client.post(ep, payload)

    return response
