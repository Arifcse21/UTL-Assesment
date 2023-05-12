from rest_framework.routers import DefaultRouter
from sales.views import CreateSalesViewSet, RetrieveSalesViewSet, GetSalesReportViewSet
from django.urls import path, include

router = DefaultRouter()

router.register("create-sale", CreateSalesViewSet, basename='create-sale')
router.register("retrieve-sale", RetrieveSalesViewSet, basename='retrieve-sale')
router.register("generate-sale-report", GetSalesReportViewSet, basename='generate-sale-report')


urlpatterns = [
    path('', include(router.urls))
]

