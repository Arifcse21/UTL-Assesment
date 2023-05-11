import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestLoginEndpoint:

    @pytest.mark.xfail
    def test_will_fail(self, api_client):
        ep = reverse('login-user-list')
        payload = {}    # no payload will raise exception

        resp = api_client.post(ep, payload)

        assert resp.status_code == 200

    def test_login_user(self, api_client, register_test_user):
        ep = reverse('login-user-list')
        payload = {
            'email': 'test_login@tesmail.com',
            'password': 'userpass1234',

        }

        resp = api_client.post(ep, payload)
        response = resp.json()

        assert response['status'] == 'successful'
        assert response['message'] == 'user logged in successfully'
        access_token = response.get('access_token')
        refresh_token = response.get('refresh_token')

        assert isinstance(access_token, str) is True
        assert isinstance(refresh_token, str) is True

        assert resp.status_code == 200

