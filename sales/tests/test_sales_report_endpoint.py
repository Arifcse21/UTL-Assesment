import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestSalesReportEndpoint:

    def test_will_fail(self, api_client):
        ep = reverse('generate-sale-report-list')

        resp = api_client.get(ep)

        response = resp.json()

        assert resp.status_code == 200
        assert response['status'] == 'successful'


