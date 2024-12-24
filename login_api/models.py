from __future__ import annotations

from django.contrib.auth.models import User
from django.db import models


class ExtendedUser(User):
    is_employee = models.BooleanField()
