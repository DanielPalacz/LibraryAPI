from __future__ import annotations

from django.contrib import admin

from .models import ExtendedUser

# Register your models here.

admin.site.register(ExtendedUser)
