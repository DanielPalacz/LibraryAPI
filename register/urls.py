from __future__ import annotations

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import logged_out
from .views import RegisterView

app_name = "register"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(http_method_names=["post"]), name="logout"),
    path("logged_out/", logged_out, name="logged_out"),
    path("register/", RegisterView.as_view(), name="register"),
]
