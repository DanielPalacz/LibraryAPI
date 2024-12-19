from __future__ import annotations

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter  # type: ignore

from .views import BookCategoryViewSet


router = DefaultRouter()
router.register(r"categories", BookCategoryViewSet)


urlpatterns = [
    path("", include(router.urls)),  # Attaching all paths generated by router
]