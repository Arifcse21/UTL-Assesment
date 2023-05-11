from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from user.serializers import RegistrationSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema


class RegistrationViewSet(ViewSet):
    """
        This ViewSet register a user with minimal user information:
         unique email, username, first_name, last_name, password, confirm password

    """

    @swagger_auto_schema(
        request_body=RegistrationSerializer,
        operation_summary="Register a new user",
        operation_description="This api creates a new user record"
    )
    def create(self, request):
        user_info = request.data
        try:

            user = get_user_model().objects.create(
                email=request.data['email'],
                username=request.data['username'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name']
            )
            if request.data['password1'] == request.data['password2']:
                user.set_password(request.data['password1'])
                user.save()
                serializer = UserSerializer(user)
                api_response = {
                    "status": "successful",
                    "message": "New user registered",
                    "data": serializer.data
                }
                return Response(api_response, status=status.HTTP_201_CREATED)
            else:
                api_response = {
                    "status": "failed",
                    "message": "Passwords do not match",
                }
                return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            api_response = {
                "status": "failed",
                "message": str(e),
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)

