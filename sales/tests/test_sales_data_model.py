import pytest
from sales.models import SalesData
from datetime import date, timedelta

pytestmark = pytest.mark.django_db


class TestSalesModel:

    def test_sale_data(self):
        c_sale = SalesData.objects.create(
            order_id="1000",
            order_date=str(date.today()),
            ship_date=str(date.today() + timedelta(days=7)),
            ship_mode="Standard Class",
            customer_id="US-1235454",
            customer_name="Lucifer Morningstar",
            segment="Corporate",
            country="Divided States",
            city="Los Devels",
            state="Hellfornia",
            postal_code="20623",
            region="North",
            product_id="FUR-FU-932853",
            category="Office Supplies",
            sub_category="Art",
            product_name="Janina vai",
            sales=500.40
        )

        query = SalesData.objects.all()
        count = query.count()
        sale = query.get(pk=1)

        assert count == 1
        assert c_sale.order_id == sale.order_id
