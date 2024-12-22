from __future__ import annotations

from django.contrib.auth.models import User
from rest_framework import serializers  # type: ignore


class UserSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = User
        fields = ("username", "email", "password")


class LoginSerializer(serializers.Serializer):  # type: ignore
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)


class MessageResponseSerializer(serializers.Serializer):  # type: ignore
    message = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):  # type: ignore
    token = serializers.CharField()


class ErrorResponseSerializer(serializers.Serializer):  # type: ignore
    error = serializers.CharField()


class ErrorDetailResponseSerializer(serializers.Serializer):  # type: ignore
    detail = serializers.CharField()


class AuthErrorResponseSerializer(serializers.Serializer):  # type: ignore
    error = serializers.CharField()
