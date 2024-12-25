from __future__ import annotations

from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission  # type: ignore
from rest_framework.request import Request  # type: ignore
from rest_framework.views import APIView  # type: ignore

from .models import ExtendedUser


class IsEmployee(BasePermission):  # type: ignore
    """
    Allows only employee to access.
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        try:
            extended_user = ExtendedUser.objects.get(id=request.user.id)
            is_employee_ = extended_user.is_employee
        except ExtendedUser.DoesNotExist:
            User.objects.get(id=request.user.id, is_superuser=True)
            is_employee_ = True  # assumption that Admin qualifies as an employee

        return request.user and request.user.is_authenticated and is_employee_
