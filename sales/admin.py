from django.contrib import admin
from sales.models import SalesData
# Register your models here.


@admin.register(SalesData)
class SalesDataAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "order_id",
        "order_date",
        "ship_date",
        "ship_mode",
        "customer_id",
        "customer_name",
        "segment",
        "country",
        "city",
        "state",
        "postal_code",
        "region",
        "product_id",
        "category",
        "sub_category",
        "product_name",
        "sales"
    ]
