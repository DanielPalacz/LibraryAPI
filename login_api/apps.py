from __future__ import annotations

from django.apps import AppConfig


class LoginApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "login_api"

    class Meta:
        app_label = "login_api"
