from __future__ import annotations

from rest_framework import viewsets  # type: ignore

from .models import Author
from .models import Book
from .models import BookCategory
from .serializers import AuthorSerializer
from .serializers import BookCategorySerializer
from .serializers import BookSerializer

# from django.shortcuts import render


class AuthorViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Author.objects.all().order_by("last_name")
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer


class BookCategoryViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = BookCategory.objects.all().order_by("name")
    serializer_class = BookCategorySerializer
