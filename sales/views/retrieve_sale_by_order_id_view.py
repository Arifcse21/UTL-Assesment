from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sales.serializers import SalesDataSerializer
from sales.models import SalesData
from drf_yasg.utils import swagger_auto_schema


class RetrieveSalesViewSet(ViewSet):
    """
        Retrieve a sale data record
    """
    @swagger_auto_schema(
        operation_summary="Retrieve a sale record using order id",
        operation_description="This api retrieve a sale record"
    )
    def retrieve(self, request, pk=None):
        try:
            queryset = SalesData.objects.filter(order_id=pk)

            sale = SalesDataSerializer(queryset, many=True)

            api_response = {
                "status": "successful",
                "message": "Sales data",
                "data": sale.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            api_response = {
                "status": "failed",
                "message": str(e)
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
