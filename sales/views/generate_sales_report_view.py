from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sales.serializers import SalesDataSerializer
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Count, Sum
from django.db.models.functions import ExtractYear
from sales.models import SalesData
import pdfkit


class GetSalesReportViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary="Retrieve sales report",
        operation_description="This api retrieve sales report"
    )
    def list(self, request):
        sales_per_year = SalesData.objects\
            .annotate(sales_year=ExtractYear('order_date'))\
            .values('sales_year').annotate(order_count=Count('*'))\
            .order_by('sales_year')

        distinct_customer_count = SalesData.objects\
            .filter(customer_id__isnull=False)\
            .values('customer_id')\
            .distinct()\
            .count()

        top_customers = SalesData.objects\
            .values('customer_id', 'customer_name')\
            .annotate(total_transactions=Sum('sales'))\
            .order_by('-total_transactions')[:3]

        customer_transactions_per_year = SalesData.objects\
            .values(year=ExtractYear('order_date'))\
            .annotate(customer_count=Count('customer_id', distinct=True))\
            .order_by('year')

        top_selling_subcategories = SalesData.objects\
            .values('sub_category')\
            .annotate(total_sales=Count('sub_category'))\
            .order_by('-total_sales')\
            .values_list('sub_category', flat=True)
        sales_performance_by_region = SalesData.objects\
            .values('region')\
            .annotate(total_sales=Sum('sales'))\
            .order_by('-total_sales')

        sales_performance_over_years = SalesData.objects\
            .values(year=ExtractYear('order_date'))\
            .annotate(total_sales=Sum('sales'))\
            .order_by('year')

        api_response = {
            "status": "successful",
            "message": "Sales Reports",
            "sales_per_year": sales_per_year,
            "distinct_customer": distinct_customer_count,
            "top_3_customer": top_customers,
            "customer_transactions_per_year": customer_transactions_per_year,
            "top_selling_subcategories": top_selling_subcategories,
            "sales_performance_by_region": sales_performance_by_region,
            "sales_performance_over_years": sales_performance_over_years
        }

        return Response(api_response, status=status.HTTP_200_OK)
