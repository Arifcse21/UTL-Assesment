import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestRegisterEndpoint:

    @pytest.mark.xfail  # who cares when fails, dhur
    def test_will_fail(self, api_client):
        ep = reverse('register-user-list')
        payload = {}    # no payload will raise exception

        resp = api_client.post(ep, payload)

        assert resp.status_code == 201

    def test_register_user(self, api_client):
        ep = reverse('register-user-list')
        payload = {
            'email': 'test_email@tesmail.com',
            'username': 'test_user',
            'password1': 'monejachaitai',
            'password2': 'monejachaitai',
            'first_name': 'test',
            'last_name': 'user'
        }

        resp = api_client.post(ep, payload)
        response = resp.json()

        assert response['status'] == 'successful'
        assert response['message'] == 'New user registered'
        assert len(response['data']) == 5

        assert resp.status_code == 201

