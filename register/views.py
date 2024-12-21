from __future__ import annotations

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiResponse
from rest_framework import status  # type: ignore
from rest_framework.exceptions import ValidationError  # type: ignore
from rest_framework.permissions import AllowAny  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore

from register.serializers import UserSerializer


class RegisterView(APIView):  # type: ignore

    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # This turns off authentication

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
    def post(self, request):  # type: ignore
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_password(password)
        except ValidationError as e:
            return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


def logged_out(request):  # type: ignore
    return render(request, "registration/user_logged_out.html", {})
