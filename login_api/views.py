from __future__ import annotations

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiResponse
from rest_framework import status  # type: ignore
from rest_framework import viewsets
from rest_framework.permissions import AllowAny  # type: ignore
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore

from login_api.serializers import UserSerializer

# from rest_framework.authentication import get_authorization_header  # type: ignore
# from rest_framework.authtoken.models import Token  # type: ignore
# from rest_framework.permissions import IsAuthenticated

# from django.contrib.auth import authenticate

# from login_api.serializers import ErrorDetailResponseSerializer
# from login_api.serializers import ErrorResponseSerializer
# from login_api.serializers import LoginSerializer
# from login_api.serializers import MessageResponseSerializer
# from login_api.serializers import TokenResponseSerializer


class RegisterView(APIView):  # type: ignore

    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # This turns off authentication

    @extend_schema(
        summary="User Registration",
        description="Endpoint to login_api a new user.",
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

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


# @extend_schema(
#     summary="User Logout",
#     description="This endpoint logs out a user, invalidating the session.",
#     methods=["POST"],  # Explicitly mention this is a POST method
#     tags=["User Management"],
#     responses={
#         200: MessageResponseSerializer,  # Use the SuccessResponseSerializer for 200 response
#         400: ErrorResponseSerializer,  # Use the ErrorResponseSerializer for 400 response
#         403: ErrorDetailResponseSerializer,  # Use the ErrorResponseSerializer for 403 response
#     },
#     request=None,  # This tells drf_spectacular there is no request body (since it’s a simple POST)
# )
# class CustomLogoutView(APIView):  # type: ignore
#     permission_classes = [IsAuthenticated]
#
#     @staticmethod
#     def post(request, *args, **kwargs):  # type: ignore
#         """
#         Call Django for Authentication Token deactivation.
#         """
#         # Extract the token from the Authorization header
#         auth_header = get_authorization_header(request).decode("utf-8")  # Get the Authorization header
#         if auth_header.startswith("Token "):  # Ensure it's a token
#             token_key = auth_header.split("Token ")[1]  # Extract the token value
#         else:
#             return Response({"error": "Invalid token format"}, status=400)
#
#         # Find the token in the database and delete it
#         try:
#             token = Token.objects.get(key=token_key)
#             token.delete()
#             return Response({"message": "Logout successful (Token deactivated)."}, status=200)
#         except Token.DoesNotExist:
#             return Response({"error": "Invalid token"}, status=400)
#
#
# @extend_schema(
#     summary="User Login",
#     description="This endpoint allows a user to log in via a JSON request and establish a session.",
#     methods=["POST"],
#     tags=["User Management"],
#     request=LoginSerializer,  # Directly associate the serializer with the request body
#     responses={
#         200: TokenResponseSerializer,  # Use the TokenResponseSerializer for 200 response
#         400: ErrorResponseSerializer,  # Use the ErrorResponseSerializer for 400 response
#     },
# )
# class CustomLoginView(APIView):  # type: ignore
#     permission_classes = [AllowAny]  # Anyone can access this view
#
#     @staticmethod
#     def post(request):  # type: ignore
#         """
#         Handles user login, establishes a session, and returns a success message.
#         """
#         # Use the LoginSerializer to validate the incoming data
#         serializer = LoginSerializer(data=request.data)
#
#         if serializer.is_valid():
#             username = serializer.validated_data.get("username")
#             password = serializer.validated_data.get("password")
#
#             # Authenticate the user
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 token, created = Token.objects.get_or_create(user=user)
#                 # Return a token response
#                 token_value = "Token " + token.key
#                 return Response({"token": token_value}, status=status.HTTP_200_OK)
#             else:
#                 # Return an error response if authentication fails
#                 return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             # Return an error if the serializer is invalid
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=["Users"],
)
class UserViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer

    permission_classes = [IsAdminUser]  # This turns off authentication
