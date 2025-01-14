from __future__ import annotations

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiResponse
from rest_framework import status  # type: ignore
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore

from .models import ExtendedUser
from .permissions import IsEmployee
from login_api.serializers import ExtendedUserSerializer

# from django.contrib.auth.models import User


@extend_schema(
    summary="User Registration",
    description="Endpoint to register a new user.",
    tags=["User Management"],
    responses={
        201: OpenApiResponse(
            description="User registered successfully",
        ),
        400: OpenApiResponse(
            description="Bad Request - Username taken or invalid password",
        ),
    },
)
class RegisterView(APIView):  # type: ignore

    serializer_class = ExtendedUserSerializer
    permission_classes = [IsEmployee]  # Setups authentication based on custom Auth class

    @staticmethod
    def post(request):  # type: ignore
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        is_employee = request.data.get("is_employee")

        if ExtendedUser.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_password(password)
        except ValidationError as e:
            return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        user = ExtendedUser.objects.create_user(
            username=username, email=email, password=password, is_employee=is_employee
        )
        user.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


@extend_schema(
    tags=["Users"],
)
class UserViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = ExtendedUser.objects.all().order_by("username")
    serializer_class = ExtendedUserSerializer

    permission_classes = [IsAdminUser]  # This turns off authentication
