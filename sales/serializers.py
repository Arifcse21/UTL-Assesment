from sales.models import SalesData
from rest_framework.serializers import ModelSerializer


class SalesDataSerializer(ModelSerializer):

    class Meta:
        model = SalesData
        fields = "__all__"

