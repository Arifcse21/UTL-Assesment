from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sales.serializers import SalesDataSerializer
from drf_yasg.utils import swagger_auto_schema


class CreateSalesViewSet(ViewSet):
    """
        Create a sales data record
    """
    @swagger_auto_schema(
        request_body=SalesDataSerializer,
        operation_summary="Insert a new sale record",
        operation_description="This api creates a new sale record"
    )
    def create(self, request):
        sale_data = request.data

        try:
            sale = SalesDataSerializer(data=sale_data)
            sale.is_valid(raise_exception=True)
            sale.save()

            api_response = {
                "status": "successful",
                "message": "New sale data created",
                "data": sale.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            api_response = {
                "status": "failed",
                "message": str(e)
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
