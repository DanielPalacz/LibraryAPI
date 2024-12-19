from __future__ import annotations

from rest_framework import viewsets  # type: ignore

from .models import BookCategory
from .serializers import BookCategorySerializer

# from django.shortcuts import render


class BookCategoryViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = BookCategory.objects.all().order_by("name")
    serializer_class = BookCategorySerializer
