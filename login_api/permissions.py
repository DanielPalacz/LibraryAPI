from __future__ import annotations

from rest_framework.permissions import BasePermission  # type: ignore
from rest_framework.request import Request  # type: ignore
from rest_framework.views import APIView  # type: ignore

from .models import ExtendedUser


class IsEmployee(BasePermission):  # type: ignore
    """
    Allows only employee to access.
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        extended_user = ExtendedUser.objects.get(id=request.user.id)
        return request.user and request.user.is_authenticated and extended_user.is_employee
