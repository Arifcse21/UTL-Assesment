import json
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from user.serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password
from drf_yasg.utils import swagger_auto_schema


class LoginViewSet(ViewSet):
    """
    Login a user with email and valid password
    """
    @swagger_auto_schema(
        request_body=LoginSerializer,
        operation_summary="Let login a new user",
        operation_description="This api let user login and return jwt tokens"
    )
    def create(self, request):
        login_data = request.data
        user = get_user_model().objects.filter(email=login_data['email'])

        if user.exists():
            user = user.first()
            check_password(login_data['password'], user.password)
            print(f"{user}")
            refresh = str(RefreshToken.for_user(user))
            access = str(AccessToken.for_user(user))

            api_response = {
                'status': 'successful',
                'message': 'user logged in successfully',
                'access_token': access,
                'refresh_token': refresh,
            }
            return Response(api_response, status=status.HTTP_200_OK)
        else:
            api_response = {
                'status': 'failed',
                'message': "Invalid credentials"
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)

