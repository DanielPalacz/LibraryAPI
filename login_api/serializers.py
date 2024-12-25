from __future__ import annotations

from rest_framework import serializers  # type: ignore

from .models import ExtendedUser


class ExtendedUserSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = ExtendedUser
        fields = ("id", "username", "email", "password", "is_employee")


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
