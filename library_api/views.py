from __future__ import annotations

from rest_framework import viewsets  # type: ignore

from .models import Author
from .models import BookCategory
from .serializers import AuthorSerializer
from .serializers import BookCategorySerializer

# from django.shortcuts import render


class BookCategoryViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = BookCategory.objects.all().order_by("name")
    serializer_class = BookCategorySerializer


class AuthorViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Author.objects.all().order_by("last_name")
    serializer_class = AuthorSerializer
