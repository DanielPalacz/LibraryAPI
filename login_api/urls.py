from __future__ import annotations

from django.urls import path

from .views import CustomLoginView
from .views import CustomLogoutView
from .views import RegisterView

app_name = "login_api"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="api-login"),
    path("logout/", CustomLogoutView.as_view(), name="api-logout"),
    path("register/", RegisterView.as_view(), name="api-register"),
]
