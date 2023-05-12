from django.db import models

# def maintain_serial():
#     last_id = SalesData.objects.all().order_by('id').last()
#     if last_id:
#         return last_id.id + 1
#     return 1


class SalesData(models.Model):
    order_id = models.CharField(max_length=500, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    ship_date = models.DateField(null=True, blank=True)
    ship_mode = models.CharField(max_length=500, null=True, blank=True)
    customer_id = models.CharField(max_length=500, null=True, blank=True)
    customer_name = models.CharField(max_length=500, null=True, blank=True)
    segment = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    postal_code = models.CharField(max_length=500, null=True, blank=True)
    region = models.CharField(max_length=500, null=True, blank=True)
    product_id = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=500, null=True, blank=True)
    sub_category = models.CharField(max_length=500, null=True, blank=True)
    product_name = models.CharField(max_length=500, null=True, blank=True)
    sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Sales Data"

    def __str__(self):
        return str(self.order_id)

