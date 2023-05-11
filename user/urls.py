from rest_framework.routers import DefaultRouter
from user.views import RegistrationViewSet, LoginViewSet
from django.urls import path, include

router = DefaultRouter()

router.register('register', RegistrationViewSet, basename='register-user')
router.register('login', LoginViewSet, basename='login-user')


urlpatterns = [
    path('', include(router.urls))
]
